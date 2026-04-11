import { useEffect, useState } from 'react';
import { rulesService } from '../services/api';
import { Link } from 'react-router-dom';
import { FiEdit2, FiTrash2, FiToggleLeft, FiToggleRight, FiPlus } from 'react-icons/fi';

const RulesList = () => {
    const [rules, setRules] = useState([]);
    const [loading, setLoading] = useState(true);

    const fetchRules = async () => {
        try {
            const data = await rulesService.getRules();
            setRules(data);
        } catch (error) {
            console.error("Error fetching rules:", error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchRules();
    }, []);

    const toggleStatus = async (rule) => {
        try {
            await rulesService.updateRule(rule.rule_id, { status: !rule.status });
            fetchRules();
        } catch (error) {
            console.error("Error toggling status", error);
        }
    };

    const deleteRule = async (id) => {
        if (!window.confirm("Are you sure you want to delete this rule?")) return;
        try {
            await rulesService.deleteRule(id);
            fetchRules();
        } catch (error) {
            console.error("Error deleting rule", error);
        }
    };

    if (loading) return <div style={{ padding: '2rem' }}>Loading rules...</div>;

    return (
        <div>
            <div className="page-header">
                <div>
                    <h1>Automation Rules</h1>
                    <p>Manage your store triggers and automatic actions</p>
                </div>
                <Link to="/rules/create" className="btn btn-primary"><FiPlus /> Create Rule</Link>
            </div>

            <div className="glass-panel table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Rule Name</th>
                            <th>Trigger</th>
                            <th>Condition</th>
                            <th>Action</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rules.map(rule => (
                            <tr key={rule.rule_id}>
                                <td style={{ fontWeight: 500 }}>{rule.rule_name}</td>
                                <td><span className="badge trigger">{rule.trigger_type}</span></td>
                                <td style={{ fontFamily: 'monospace', color: 'var(--text-muted)' }}>{rule.condition}</td>
                                <td>{rule.action_type.replace('_', ' ')}</td>
                                <td>
                                    <span className={`badge ${rule.status ? 'active' : 'inactive'}`}>
                                        {rule.status ? 'Active' : 'Disabled'}
                                    </span>
                                </td>
                                <td>
                                    <div style={{ display: 'flex', gap: '0.75rem' }}>
                                        <button 
                                            onClick={() => toggleStatus(rule)}
                                            style={{ background: 'none', border: 'none', color: rule.status ? 'var(--success)' : 'var(--text-muted)', cursor: 'pointer', fontSize: '1.25rem' }}
                                            title="Toggle Status"
                                        >
                                            {rule.status ? <FiToggleRight /> : <FiToggleLeft />}
                                        </button>
                                        <button 
                                            onClick={() => deleteRule(rule.rule_id)}
                                            style={{ background: 'none', border: 'none', color: 'var(--danger)', cursor: 'pointer', fontSize: '1.1rem' }}
                                            title="Delete"
                                        >
                                            <FiTrash2 />
                                        </button>
                                    </div>
                                </td>
                            </tr>
                        ))}
                        {rules.length === 0 && (
                            <tr>
                                <td colSpan="6" style={{ textAlign: 'center', padding: '3rem' }}>No rules found. Create one to get started!</td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default RulesList;
