
import styles from './App.css';

// import {useState} from "react";
// import Chart from "./Chart";
// import Demo from './demo';
// import Video from "./Video";
import NavBar, {Nav} from "./NavBar"

import FadeMedia from './FadeMedia'; // Import the new component
// import CoolStaff from "./CoolStaff";
// import About from "./About";
// import {ParagraphsContainer} from "./Paragraph";
// import Video from "./Video";
import {GPT, Log, LogIn, Reg, Register} from "./LogIn";
import About from "./About";
import Video from "./Video";
import {ParagraphsContainer} from "./Paragraph";
import MovingText from "./MovingText";
// import CoolStaff from "./CoolStaff";
// import Try from './Try';
function App() {
    return (
        <>
            {/*<p>hello world</p>*/}
            {/*<Video/>*/}
            {/*<About/>*/}
            {/*<FadeMedia /> /!* Use the FadeMedia component here *!/*/}
            {/*<NavBar/>*/}
            {/*<ParagraphsContainer/>*/}
            {/*<LogIn/>*/}
            {/*<Register/>*/}
            {/*<Reg/>*/}
            {/*            <MovingText text="This is my scrolling text. You can add any data you want here!" />*/}
            <Nav/>

            {/*<Log/>>*/}
            {/*<GPT/>*/}
            {/*      <Try />*/}
            {/*<CoolStaff/>*/}
            {/* <Demo logo={logo} /> */}

        </>
    );
}

export default App;
