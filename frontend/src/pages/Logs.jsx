import { useEffect, useState } from 'react';
import { rulesService } from '../services/api';

const Logs = () => {
    const [logs, setLogs] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchLogs = async () => {
            try {
                const data = await rulesService.getLogs();
                setLogs(data);
            } catch (error) {
                console.error("Error fetching logs", error);
            } finally {
                setLoading(false);
            }
        };
        
        fetchLogs();
        // Option: set interval to refresh logs
        const interval = setInterval(fetchLogs, 15000);
        return () => clearInterval(interval);
    }, []);

    if (loading) return <div style={{ padding: '2rem' }}>Loading execution logs...</div>;

    return (
        <div>
            <div className="page-header">
                <div>
                    <h1>Execution Logs</h1>
                    <p>History of automated actions executed by the scheduler</p>
                </div>
            </div>

            <div className="glass-panel table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>Time</th>
                            <th>Rule ID</th>
                            <th>Status</th>
                            <th>Message</th>
                        </tr>
                    </thead>
                    <tbody>
                        {logs.map((log) => (
                            <tr key={log.log_id}>
                                <td>{new Date(log.timestamp + 'Z').toLocaleString()}</td>
                                <td>#{log.rule_id}</td>
                                <td>
                                    <span className={`badge ${log.status === 'success' ? 'active' : 'danger'}`} style={log.status === 'error' ? { background: 'rgba(239, 68, 68, 0.1)', color: 'var(--danger)', border: '1px solid rgba(239, 68, 68, 0.3)' } : {}}>
                                        {log.status}
                                    </span>
                                </td>
                                <td style={{ color: 'var(--text-muted)' }}>{log.message}</td>
                            </tr>
                        ))}
                        {logs.length === 0 && (
                            <tr>
                                <td colSpan="4" style={{ textAlign: 'center', padding: '3rem' }}>No logs yet. The scheduler runs periodically.</td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default Logs;
