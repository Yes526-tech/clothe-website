import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import AuthPage from './components/Auth/AuthPage';
import AdminLayout from './components/Admin/AdminLayout';
import Dashboard from './components/Admin/Dashboard';
import Inventory from './components/Admin/Inventory';
import Customers from './components/Admin/Customers';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/auth" element={<AuthPage />} />
        
        <Route path="/admin" element={<AdminLayout><Dashboard /></AdminLayout>} />
        <Route path="/admin/inventory" element={<AdminLayout><Inventory /></AdminLayout>} />
        <Route path="/admin/customers" element={<AdminLayout><Customers /></AdminLayout>} />
        
        <Route path="*" element={<Navigate to="/auth" />} />
      </Routes>
    </Router>
  );
}

export default App;
