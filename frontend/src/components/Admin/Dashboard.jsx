import React, { useEffect, useState } from 'react';
import { DollarSign, ShoppingBag, AlertCircle, TrendingUp } from 'lucide-react';

const MetricCard = ({ title, value, icon, trend }) => (
  <div className="bg-white rounded-xl p-6 shadow-sm border border-burgundy-900/10 flex items-start justify-between relative overflow-hidden group hover:shadow-md transition-shadow">
    <div className="absolute top-0 right-0 -mt-4 -mr-4 w-24 h-24 bg-gold-500/10 rounded-full blur-xl group-hover:bg-gold-500/20 transition-colors"></div>
    <div>
      <p className="text-sm font-serif italic text-burgundy-900/60 mb-1">{title}</p>
      <h3 className="text-3xl font-serif text-burgundy-900">{value}</h3>
      <p className="text-xs font-sans text-emerald-700 mt-2 flex items-center">
        <TrendingUp size={12} className="mr-1" /> {trend}
      </p>
    </div>
    <div className="p-3 bg-burgundy-900/5 rounded-lg text-gold-600">
      {icon}
    </div>
  </div>
);

const Dashboard = () => {
  const [metrics, setMetrics] = useState({ totalWealth: 0, totalProducts: 0, lowStockAlerts: 0 });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/admin/metrics')
      .then(res => res.json())
      .then(data => {
        setMetrics(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching metrics:", err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-serif text-burgundy-900">Grand Ledger</h1>
        <button className="px-4 py-2 bg-emerald-700 text-parchment-100 font-serif text-sm rounded shadow-sm hover:bg-emerald-900 transition-colors">
          Download Report
        </button>
      </div>

      {loading ? (
        <div className="text-center py-10 font-serif italic text-burgundy-900">Consulting the archives...</div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <MetricCard title="Total Wealth" value={`${metrics.totalWealth.toLocaleString()} G`} icon={<DollarSign />} trend="Inventory Value" />
          <MetricCard title="Catalog Size" value={metrics.totalProducts} icon={<ShoppingBag />} trend="Unique Items" />
          <MetricCard title="Low Stock Alerts" value={`${metrics.lowStockAlerts} Items`} icon={<AlertCircle className="text-red-600" />} trend="Requires action" />
          <MetricCard title="Pending Orders" value="0" icon={<TrendingUp />} trend="Coming Soon" />
        </div>
      )}

      {/* Chart Placeholder */}
      <div className="mt-8 bg-white rounded-xl shadow-sm border border-burgundy-900/10 p-6">
        <h2 className="text-xl font-serif text-burgundy-900 mb-6">Revenue Trajectory</h2>
        <div className="h-72 w-full bg-parchment-200/50 rounded-lg flex items-center justify-center border border-dashed border-burgundy-900/20">
          <p className="text-burgundy-900/40 font-serif italic">[ Elegant Chart Visualization Renders Here ]</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
