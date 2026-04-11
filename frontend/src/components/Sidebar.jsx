import { NavLink, useNavigate } from 'react-router-dom';
import { authService } from '../services/api';
import { FiHome, FiList, FiPlusSquare, FiActivity, FiPieChart, FiLogOut, FiZap } from 'react-icons/fi';

const Sidebar = () => {
    const navigate = useNavigate();

    const handleLogout = () => {
        authService.logout();
        navigate('/login');
    };

    return (
        <aside className="sidebar glass-panel" style={{ borderTopLeftRadius: 0, borderBottomLeftRadius: 0, borderTopRightRadius: 16, borderBottomRightRadius: 16 }}>
            <div className="logo">
                <FiZap style={{ color: 'var(--primary)' }} />
                AutoFlow
            </div>
            
            <nav className="nav-links">
                <NavLink to="/dashboard" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                    <FiHome /> Dashboard
                </NavLink>
                <NavLink to="/rules" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`} end>
                    <FiList /> Rules List
                </NavLink>
                <NavLink to="/rules/create" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                    <FiPlusSquare /> Create Rule
                </NavLink>
                <NavLink to="/logs" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                    <FiActivity /> Execution Logs
                </NavLink>
                <NavLink to="/reports" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                    <FiPieChart /> Reports
                </NavLink>
            </nav>

            <div style={{ marginTop: 'auto' }}>
                <button 
                  onClick={handleLogout} 
                  className="nav-link" 
                  style={{ background: 'transparent', border: 'none', width: '100%', cursor: 'pointer', textAlign: 'left' }}
                >
                    <FiLogOut /> Logout
                </button>
            </div>
        </aside>
    );
};

export default Sidebar;
