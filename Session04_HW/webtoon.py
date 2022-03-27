def extract_info(webtoon_list):
    result = []

    for webtoon in webtoon_list:
       
        title = webtoon.find("dt").find("a").text
        artist = webtoon.find("dd", {"class":"desc"}).find("a").text
        rating = webtoon.find("strong").text

        webtoon_info = {
            'title' : title,
            'artist' : artist,
            'rating' : rating,
        }
        result.append(webtoon_info)
    
    return result


