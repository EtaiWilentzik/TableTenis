import './NavBar.css';

const NavBar = () => {

    return (
        <>
            <div id="menu">
                <div id="menu-items">
                    <div className="menu-item">Log in</div>
                    <div className="menu-item">Register</div>
                    <div className="menu-item">About</div>
                </div>

            </div>

        </>
    );

}

// im using the color of the menu as the ping pong racket one is red one is blue
const Nav = () => {
    return (
        <>
            <nav className="navbar navbar-expand-lg navbar-light " id="navbar">
                <div className="container-fluid" id="nav">
                    {/*<a className="navbar-brand" href="#">Navbar</a>*/}

                    <a className="navbar-brand d-flex align-items-center" href="#">
                        <img
                            src={"logo.jpg"}
                            alt="Logo"
                            style={{height: '8rem', marginRight: '10px'}}
                        />
                    </a>

                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse"
                            data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false"
                            aria-label="Toggle navigation">

                        <span className="navbar-toggler-icon bg-danger"></span>
                    </button>


                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav ms-auto">
                            <li className="nav-item">
                                <a className="nav-link active" aria-current="page" href="#">Home</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link active" href="#">Features</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link active" href="#">Pricing</a>
                            </li>

                        </ul>
                    </div>
                </div>
            </nav>
        </>
    )
        ;
};


export {NavBar, Nav}
