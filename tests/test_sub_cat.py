from models.souscategorieModel import SousCategorieModel


def test_sub_cat_creation():
    sub_cat = SousCategorieModel('Disques durs', 'https://www.alibaba.com/trade/search?spm=a27aq.cp_44.4746171840.1.61f93ccfIVG0Go&categoryId=711001&SearchText=Disques+durs&indexArea=product_en&fsb=y&productId=1600896969230')
    print(sub_cat.creer_dossier, "testesr")
    assert sub_cat.nom == 'Disques durs'

def test_sub_cat_folder_creation():
    sub_cat = SousCategorieModel('Disques durs', 'https://www.alibaba.com/trade/search?spm=a27aq.cp_44.4746171840.1.61f93ccfIVG0Go&categoryId=711001&SearchText=Disques+durs&indexArea=product_en&fsb=y&productId=1600896969230')
    assert sub_cat.creer_dossier("C:/Users/sk/Desktop/Master GL/Scraping-Alibaba-main/Scraping-Alibaba-main/Data/") == 'C:/Users/sk/Desktop/Master GL/Scraping-Alibaba-main/Scraping-Alibaba-main/Data/Disques durs'

