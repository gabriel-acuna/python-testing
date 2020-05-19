import unittest
from shopping_cart import Item, ShoppingCart, NotExistsItemError

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.bread = Item('Bread', 3.5)
        self.beer = Item('Beer', 1.75)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item({'item':self.bread, 'quantity': 2})

    def tearDown(self):
        pass

    def test_item_name_eq_bread(self):
        self.assertEqual(self.bread.name, 'Bread')

    def test_item_name_dif_bread(self):
        self.assertNotEqual(self.beer.name, 'Bread')

    def test_shopping_cart_has_item_bread(self):
        self.assertTrue(self.shopping_cart.contains_item())
    
    def test_shopping_cart_has_no_item(self):
        self.shopping_cart.remove_item(self.bread)
        self.assertFalse(self.shopping_cart.contains_item())
    
    def test_shopping_cart_get_item_bread(self):
        item = self.shopping_cart.get_item(self.bread)
        self.assertIs(item, self.bread)

    def test_get_item_exception(self):
        with self.assertRaises(NotExistsItemError):
            self.shopping_cart.get_item(self.beer)

    def test_get_total_eq_seven(self):
        self.assertGreater(self.shopping_cart.total(), 0)
        self.assertLessEqual(self.shopping_cart.total(), 7.0)

    def test_item_code(self):
        self.assertRegex(self.beer.code(), self.beer.name)

    def test_clear_cart(self):
        self.shopping_cart.clear_cart()
        self.assertFalse(self.shopping_cart.contains_item())
    def test_fail(self):
        if 2**0.5 > 1:
            self.fail('The square rooot of 2 is greater than 1')

    #@unittest.skip('Not implemented ')
    @unittest.skipIf( True, ' Shopping Cart has items')
    def test_skip(self):
        pass

if __name__ == '__main__':
    unittest.main()