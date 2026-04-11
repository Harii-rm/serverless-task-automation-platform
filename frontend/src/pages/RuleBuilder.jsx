import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { rulesService } from '../services/api';

const RuleBuilder = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        rule_name: '',
        trigger_type: 'threshold',
        condition: '',
        action_type: 'notify_admin',
        parameters: '{}',
        status: true
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await rulesService.createRule(formData);
            navigate('/rules');
        } catch (error) {
            console.error("Error creating rule", error);
            alert("Failed to create rule");
        }
    };

    return (
        <div>
            <div className="page-header">
                <div>
                    <h1>Create Automation Rule</h1>
                    <p>Setup a new trigger and action for your store</p>
                </div>
            </div>

            <div className="glass-panel" style={{ padding: '2rem', maxWidth: '800px' }}>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label className="form-label">Rule Name</label>
                        <input 
                            type="text" 
                            name="rule_name" 
                            className="form-control" 
                            value={formData.rule_name} 
                            onChange={handleChange} 
                            required 
                            placeholder="e.g. Low Stock Warning"
                        />
                    </div>
                    
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
                        <div className="form-group">
                            <label className="form-label">Trigger Type</label>
                            <select name="trigger_type" className="form-control" value={formData.trigger_type} onChange={handleChange}>
                                <option value="threshold">Threshold (e.g. stock level)</option>
                                <option value="behavior">Behavior (e.g. inactive cart)</option>
                                <option value="time">Time-based (e.g. schedule)</option>
                                <option value="event">Event-based (e.g. order placed)</option>
                            </select>
                        </div>
                        <div className="form-group">
                            <label className="form-label">Trigger Condition</label>
                            <input 
                                type="text" 
                                name="condition" 
                                className="form-control" 
                                value={formData.condition} 
                                onChange={handleChange} 
                                required 
                                placeholder="e.g. stock < 10 or cart inactive 30 min"
                            />
                        </div>
                    </div>

                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
                        <div className="form-group">
                            <label className="form-label">Action</label>
                            <select name="action_type" className="form-control" value={formData.action_type} onChange={handleChange}>
                                <option value="notify_admin">Notify Admin</option>
                                <option value="send_email">Send Email (Simulated)</option>
                                <option value="generate_report">Generate Report</option>
                                <option value="apply_discount">Apply Discount</option>
                            </select>
                        </div>
                        <div className="form-group">
                            <label className="form-label">Action Parameters (JSON)</label>
                            <input 
                                type="text" 
                                name="parameters" 
                                className="form-control" 
                                value={formData.parameters} 
                                onChange={handleChange} 
                                placeholder='{"email": "admin@store.com"}'
                            />
                        </div>
                    </div>

                    <div className="form-group" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        <label className="form-label" style={{ marginBottom: 0 }}>Active upon creation?</label>
                        <input 
                            type="checkbox" 
                            name="status" 
                            checked={formData.status} 
                            onChange={(e) => setFormData({ ...formData, status: e.target.checked })}
                            style={{ transform: 'scale(1.2)' }}
                        />
                    </div>

                    <div style={{ display: 'flex', gap: '1rem', marginTop: '2rem' }}>
                        <button type="submit" className="btn btn-primary">Save Rule</button>
                        <button type="button" className="btn btn-secondary" onClick={() => navigate('/rules')}>Cancel</button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default RuleBuilder;
