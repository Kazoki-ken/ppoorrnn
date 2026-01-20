# -*- coding: UTF-8 -*-

from .core import *

class Stars(object):

    def __init__(self, ProxyDictionary, *args):
        self.ProxyDictionary = ProxyDictionary

    def _sortStars(self, sort_by):
        sort_dict = dict()

        if not sort_by:
            return sort_dict

        sort_types = {"view": "mv", "trend": "t", "subs": "ms", "alpha": "a", "videos": "nv", "random": "r"}

        for key in sort_types:
            if key in sort_by.lower():
                sort_dict["o"] = sort_types[key]
                return sort_dict

        return sort_dict

    def _craftStarsPage(self, page_num, sort_by):
        payload = dict()

        stars_sort = self._sortStars(sort_by)
        for key in stars_sort:
            payload[key] = stars_sort[key]

        payload["page"] = page_num
        return payload

    def _loadStarsPage(self, page_num, sort_by):

        r = requests.get(BASE_URL + PORNSTARS_URL, params=self._craftStarsPage(page_num, sort_by), headers=HEADERS, proxies=self.ProxyDictionary)
        html = r.text

        return BeautifulSoup(html, "lxml")

    def _scrapLiStars(self, soup_data):
        # get div with list of stars (month popular is the 1st)
        # Updated selector as per recent PornHub HTML changes
        popular_ul = soup_data.find(id="popularPornstars")
        if popular_ul:
            return popular_ul.find_all("li")

        # Fallback to old method just in case, but it seemed to pick up filters instead of stars
        div_el = soup_data.find("div", { "class" : "sectionWrapper", "id" : "pornstarsFilterContainer" } )
        if div_el:
             # This container usually contains filters, not stars, but keeping it as fallback logic or for other pages
             return div_el.find_all("li")

        return []

    def _scrapStarInfo(self, li_el):
        data = {
            "name"          : None,         # string
            "rank"          : None,         # integer
            "type"          : None,         # string
            "videos"        : None,         # integer
            "views"         : None,         # string
            "verified"      : False,        # bool
            "trophy"        : False,        # bool
            "url"           : None,         # string
            "photo"         : None,         # string
        }

        # scrap rank
        for span_tag in li_el.find_all("span", class_="rank_number"):
            try:
                data["rank"] = int(span_tag.text)
            except Exception as e:
                pass

        # scrap name and url
        for a_tag in li_el.find_all("a", href=True):
            try:
                url = a_tag.attrs["href"]
                if isStar(url):
                    data["url"] = BASE_URL + url
                    # data-mxptext might be missing, try text or alt from img
                    data["name"] = a_tag.attrs.get("data-mxptext")
                    if not data["name"]:
                         # Try finding name inside span or img alt
                         img = a_tag.find("img")
                         if img:
                             data["name"] = img.attrs.get("alt")

                         if not data["name"]:
                             name_span = li_el.find("span", class_="performerCardName")
                             if name_span:
                                 # This often contains extra text like newlines, badges, so we need to clean it
                                 # Usually the name is just the text of the span, maybe with child spans for lastName
                                 data["name"] = " ".join(name_span.stripped_strings)

                    break
            except Exception as e:
                pass

        # scrap photo url
        for img_tag in li_el.find_all("img", src=True):
            try:
                # Updated attribute check
                photo_url = img_tag.attrs.get("data-thumb_url") or img_tag.attrs.get("src")
                if isStarPhoto(photo_url):
                    data["photo"] = photo_url
                    break
            except Exception as e:
                pass

        # scrap num of videos and views
        # Updated selector logic: The class name might just be 'videosNumber' or inside 'performerVideosViewsCount'
        # In the provided HTML, it is span.videosNumber.performerCount
        # and span.viewsNumber.performerCount

        try:
            videos_span = li_el.find("span", class_="videosNumber")
            if videos_span:
                 # Text is "277 Videos "
                 data["videos"] = int(videos_span.get_text(strip=True).split()[0])

            views_span = li_el.find("span", class_="viewsNumber")
            if views_span:
                 # Text is "467M Views "
                 data["views"] = views_span.get_text(strip=True).split()[0]
        except Exception as e:
            pass

        # scrap badges
        # Updated selector: class="modelBadges performerBadges" or just searching for icons
        # The icons are often nested deep.

        if li_el.select(".verifiedIcon"):
            data["verified"] = True

        if li_el.select(".trophyPornStar") or li_el.select(".bg-trophy-channel"):
            data["trophy"] = True

        # scrap type
        try:
            if data["url"]:
                if "pornstar" in data["url"]:
                    data["type"] = "pornstar"
                else:
                    data["type"] = "model"
        except Exception as e:
                pass

        # return
        # Relaxed check: Return data if name and url are found, even if others are missing
        if data["name"] and data["url"]:
            return data
        return False

    def getStars(self, quantity = 1, page = 1, sort_by=None, infinity = False):
        """
        Get pornstar's basic informations.

        :param quantity: number of pornstars to return
        :param page: starting page number
        :param infinity: never stop downloading
        """

        quantity = quantity if quantity >= 1 else 1
        page = page if page >= 1 else 1
        found = 0

        while True:

            for possible_star in self._scrapLiStars(self._loadStarsPage(page, sort_by)):
                data_dict = self._scrapStarInfo(possible_star)

                if data_dict:
                    yield data_dict

                    if not infinity:
                        found += 1
                        if found >= quantity: return

            page += 1
