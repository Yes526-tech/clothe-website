const express = require('express');
const path = require('path');
const pageController = require('./controllers/pageController');

const app = express();
const PORT = process.env.PORT || 3000;

const { sequelize, Product } = require('./models/Product');

// Sync SQLite database
sequelize.sync()
  .then(() => console.log('✅ SQLite database synced successfully'))
  .catch(err => console.error('❌ SQLite sync error:', err));

// Middleware
app.use(express.json());

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));
// Serve React app static files
app.use(express.static(path.join(__dirname, 'frontend/dist'), { index: false }));

// Set up routes to be handled by the controller
app.get('/', pageController.getIndex);
app.get('/men', pageController.getMen);
app.get('/women', pageController.getWomen);
app.get('/collection/medieval', pageController.getMedieval);
app.get('/collection/graffiti', pageController.getGraffiti);
app.get('/collection/sweatshirt', pageController.getSweatshirt);
app.get('/collections', pageController.getCollections);

// Serve React SPA for Auth and Admin
app.get(['/auth', /^\/admin(\/.*)?$/], (req, res) => {
  res.sendFile(path.join(__dirname, 'frontend/dist/index.html'));
});

// --- API ROUTES ---
app.get('/api/products', async (req, res) => {
  try {
    const { category, collectionName } = req.query;
    const filter = {};
    if (category) filter.category = category;
    if (collectionName) filter.collectionName = collectionName;
    
    const products = await Product.findAll({ where: filter });
    res.json(products);
  } catch (error) {
    console.error('API Error:', error);
    res.status(500).json({ error: 'Server error fetching products' });
  }
});

app.post('/api/products', async (req, res) => {
  try {
    const product = await Product.create(req.body);
    res.status(201).json(product);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.put('/api/products/:id', async (req, res) => {
  try {
    const product = await Product.findByPk(req.params.id);
    if (!product) return res.status(404).json({ error: 'Not found' });
    await product.update(req.body);
    res.json(product);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.delete('/api/products/:id', async (req, res) => {
  try {
    const product = await Product.findByPk(req.params.id);
    if (!product) return res.status(404).json({ error: 'Not found' });
    await product.destroy();
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.get('/api/admin/metrics', async (req, res) => {
  try {
    const products = await Product.findAll();
    const totalWealth = products.reduce((sum, p) => sum + (p.price * (p.stock || 0)), 0);
    const lowStockAlerts = products.filter(p => p.stock < 10).length;
    res.json({
      totalWealth,
      totalProducts: products.length,
      lowStockAlerts
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
