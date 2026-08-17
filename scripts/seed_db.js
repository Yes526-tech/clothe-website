const { sequelize, Product } = require('../models/Product');

const seedProducts = [
  // Men's Products
  { name: 'Hoodies', price: 1500, imageUrl: '/assets/images/prod_sweatshirt.png', category: 'men' },
  { name: 'Tracksuits', price: 1500, imageUrl: '/assets/images/cat_outerwear_men.png', category: 'men' },
  { name: 'Tees', price: 1500, imageUrl: '/assets/images/prod_tshirt.png', category: 'men' },
  { name: 'Accessories', price: 1500, imageUrl: '/assets/images/prod_hat.png', category: 'men' },
  { name: 'Jackets', price: 1500, imageUrl: '/assets/images/cat_knitwear_men.png', category: 'men' },
  { name: 'Extras', price: 1500, imageUrl: '/assets/images/cat_shirts_men.png', category: 'men' },
  
  // Women's Products
  { name: 'Outerwear', price: 1500, imageUrl: '/assets/images/cat_outerwear.png', category: 'women' },
  { name: 'Knitwear', price: 1500, imageUrl: '/assets/images/cat_knitwear.png', category: 'women' },
  { name: 'Dresses', price: 1500, imageUrl: '/assets/images/women_category.png', category: 'women' },
  { name: 'Tops', price: 1500, imageUrl: '/assets/images/cat_tops.png', category: 'women' },
  { name: 'Bottoms', price: 1500, imageUrl: '/assets/images/cat_bottoms.png', category: 'women' },
  { name: 'Accessories', price: 1500, imageUrl: '/assets/images/cat_accessories.png', category: 'women' },
  
  // Collection: Medieval
  { name: 'Velvet Corset Dress', price: 2500, imageUrl: '/assets/images/collections/medival2.jpg', category: 'collection', collectionName: 'medieval' },
  { name: 'Knight Wool Coat', price: 3200, imageUrl: '/assets/images/collections/medival3.jpg', category: 'collection', collectionName: 'medieval' },
  { name: 'Royal Silk Blouse', price: 1800, imageUrl: '/assets/images/collections/medival4.jpg', category: 'collection', collectionName: 'medieval' },
  { name: 'Gothic Lace Skirt', price: 1500, imageUrl: '/assets/images/collections/medival1.jpg', category: 'collection', collectionName: 'medieval' },
  
  // Collection: Graffiti
  { name: 'Urban Spray Puffer', price: 4200, imageUrl: '/assets/images/collections/grafitti2.jpg', category: 'collection', collectionName: 'graffiti' },
  { name: 'Tag Print Hoodie', price: 1800, imageUrl: '/assets/images/collections/grafitti3.jpg', category: 'collection', collectionName: 'graffiti' },
  { name: 'Distressed Denim', price: 2100, imageUrl: '/assets/images/collections/grafitti4.jpg', category: 'collection', collectionName: 'graffiti' },
  { name: 'Neon Accent Vest', price: 1950, imageUrl: '/assets/images/collections/grafitti1.jpg', category: 'collection', collectionName: 'graffiti' },
  
  // Collection: Sweatshirt
  { name: 'Heavyweight Crew', price: 1200, imageUrl: '/assets/images/collections/sweattshirt2.jpg', category: 'collection', collectionName: 'sweatshirt' },
  { name: 'Essential Zip Hoodie', price: 1500, imageUrl: '/assets/images/collections/sweattshirt3.jpg', category: 'collection', collectionName: 'sweatshirt' },
  { name: 'Lounge Sweatpants', price: 1100, imageUrl: '/assets/images/collections/sweattshirt4.jpg', category: 'collection', collectionName: 'sweatshirt' },
  { name: 'Fleece Lined Pullover', price: 1350, imageUrl: '/assets/images/collections/sweattshirt1.jpg', category: 'collection', collectionName: 'sweatshirt' }
];

async function seed() {
  try {
    await sequelize.authenticate();
    console.log('✅ Connected to SQLite database');

    await sequelize.sync({ force: true });
    console.log('🗑️ Dropped existing tables and re-synced');

    console.log('🌱 Seeding new products...');
    await Product.bulkCreate(seedProducts);

    console.log('🎉 Database seeded successfully!');
  } catch (error) {
    console.error('❌ Error seeding database:', error);
  } finally {
    await sequelize.close();
  }
}

seed();
