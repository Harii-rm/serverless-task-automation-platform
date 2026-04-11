import { useEffect, useState } from 'react';
import { rulesService } from '../services/api';
import { FiActivity, FiLayers, FiAlertCircle, FiCheckCircle } from 'react-icons/fi';
import { Link } from 'react-router-dom';

const Dashboard = () => {
    const [stats, setStats] = useState({ total_rules: 0, active_rules: 0, recent_executions: 0, alerts: 0 });
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchStats = async () => {
            try {
                const data = await rulesService.getDashboardStats();
                setStats(data);
            } catch (error) {
                console.error("Error fetching stats:", error);
            } finally {
                setLoading(false);
            }
        };
        fetchStats();
    }, []);

    if (loading) return <div style={{ padding: '2rem' }}>Loading dashboard...</div>;

    return (
        <div>
            <div className="page-header">
                <div>
                    <h1>Dashboard</h1>
                    <p>Overview of your automation platform</p>
                </div>
                <Link to="/rules/create" className="btn btn-primary">Create New Rule</Link>
            </div>

            <div className="stats-grid">
                <div className="glass-panel stat-card">
                    <div className="stat-title"><FiLayers /> Total Rules</div>
                    <div className="stat-value">{stats.total_rules}</div>
                </div>
                <div className="glass-panel stat-card" style={{ borderColor: 'rgba(16, 185, 129, 0.3)' }}>
                    <div className="stat-title"><FiCheckCircle color="var(--success)" /> Active Rules</div>
                    <div className="stat-value">{stats.active_rules}</div>
                </div>
                <div className="glass-panel stat-card">
                    <div className="stat-title"><FiActivity color="var(--primary)" /> Executions</div>
                    <div className="stat-value">{stats.recent_executions}</div>
                </div>
                <div className="glass-panel stat-card" style={{ borderColor: 'rgba(239, 68, 68, 0.3)' }}>
                    <div className="stat-title"><FiAlertCircle color="var(--danger)" /> Alerts (Low Stock)</div>
                    <div className="stat-value">{stats.alerts}</div>
                </div>
            </div>

            <div className="glass-panel" style={{ padding: '2rem', marginTop: '2rem' }}>
                <h3>Quick Actions</h3>
                <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
                    <Link to="/rules" className="btn btn-secondary">Manage Rules</Link>
                    <Link to="/logs" className="btn btn-secondary">View Execution Logs</Link>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
