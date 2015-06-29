import products
from products import groupedProducts

print dir(products)

productMap = groupedProducts()

print products.mostPopularProduct(productMap)
print products.leastPopularProduct(productMap)