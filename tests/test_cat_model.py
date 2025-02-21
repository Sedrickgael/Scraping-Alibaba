from models.categorieModel import CategorieModel


def test_cat_creation():
    model = CategorieModel('Accessoires', 'https://www.alibaba.com/Consumer-Electronics_p44')
    assert model.nom == 'Accessoires'
