class Product {
    constructor(id, name, price, imageUrl) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.imageUrl = imageUrl;
    }

    // Dummy method to simulate fetching from a database
    static getBestSellers() {
        return [
            new Product(1, 'Olive Oversized Tee', 899, '/assets/images/product1.png'),
            new Product(2, 'Explorer Graphic Tee', 799, '/assets/images/product2.png'),
            new Product(3, 'Classic Black Tee', 749, '/assets/images/product3.png'),
            new Product(4, 'Cream Essential Tee', 849, '/assets/images/product4.png')
        ];
    }
}

module.exports = Product;
