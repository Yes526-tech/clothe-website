const path = require('path');
const Product = require('../models/productModel');

// Helper function to resolve view paths
const getViewPath = (viewName) => path.join(__dirname, '../views', viewName);

exports.getIndex = (req, res) => {
    // In a real MVC, we might fetch products from the Model and pass them to a templating engine
    // const bestSellers = Product.getBestSellers();
    res.sendFile(getViewPath('index_view.html'));
};

exports.getMen = (req, res) => {
    res.sendFile(getViewPath('men_view.html'));
};

exports.getWomen = (req, res) => {
    res.sendFile(getViewPath('women_view.html'));
};

exports.getMedieval = (req, res) => {
    res.sendFile(getViewPath('medieval_view.html'));
};

exports.getGraffiti = (req, res) => {
  res.sendFile(path.join(__dirname, '../views/graffiti_view.html'));
};

exports.getSweatshirt = (req, res) => {
  res.sendFile(path.join(__dirname, '../views/sweatshirt_view.html'));
};

exports.getCollections = (req, res) => {
  res.sendFile(path.join(__dirname, '../views/collections_view.html'));
};
