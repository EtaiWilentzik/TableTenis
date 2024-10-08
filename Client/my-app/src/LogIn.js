import  "./LogIn.css"

const LogIn=()=>{
    return (

  <>
      {/*the d flex put it in the center the input group make sure everything is on the same height inside the line*/}
      <div className="d-flex align-items-center flex-column change ">
          <h2 className="display-4 mb-5">Log in</h2>
          {/* input group make sure everything is on the same height inside the line w-25 makes it 25 width of the view window*/}
          <div className="input-group mb-5  ">
              <span className="input-group-text"><i className="bi bi-person"></i></span>
              <div className="form-floating">
                  <input type="text" className="form-control" id="floatingInputGroup1" placeholder="Username"/>
                  <label htmlFor="floatingInputGroup1">Username</label>
              </div>
          </div>

          <div className="input-group mb-5 ">
              <span className="input-group-text"> <i className="bi bi-lock-fill"></i></span>
              <div className="form-floating">
                  <input type="password" className="form-control" id="floatingInputGroup1" placeholder="Password"/>
                  <label htmlFor="floatingInputGroup1">Password</label>
              </div>
          </div>
          <p><a href="#" className="text-secondary">Does not have account Register here</a></p>

          <div className="a">
              <button type="submit" className=" mb-5 btn btn-primary">Log in</button>
          </div>


      </div>
  </>

    )

}


const Register = () => {
    return (
        <>
            <div className="d-flex align-items-center flex-column change aaaa">
                <h2 className="display-4 mb-5  ">Register</h2>
                <div className="input-group mb-5 w-75">
                    <span className="input-group-text"><i className="bi bi-person"></i></span>
                    <div className="form-floating">
                        <input type="text" className="form-control" id="floatingInputGroup1" placeholder="Username"/>
                        <label htmlFor="floatingInputGroup1">Username</label>
                    </div>
                </div>

                <div className="input-group mb-5 w-75 ">
                    <span className="input-group-text"><i className="bi bi-envelope"></i></span>
                    <div className="form-floating">
                        <input type="text" className="form-control" id="floatingInputGroup1" placeholder="Email"/>
                        <label htmlFor="floatingInputGroup1">Email</label>
                    </div>
                </div>

                <div className="input-group mb-5 w-75">
                    <span className="input-group-text"><i className="bi bi-lock-fill"></i></span>
                    <div className="form-floating">
                        <input type="password" className="form-control" id="floatingInputGroup3"
                               placeholder="Password"/>
                        <label htmlFor="floatingInputGroup1">Password</label>
                    </div>
                </div>
                <div className="a">
                    <button type="submit" className="btn btn-primary mb-5">Register</button>
                </div>
            </div>
        </>
    );
}

const Reg = () => {
    return (
        <div className="container">
            <div className="row justify-content-center row-equal-height">
                <div className=" col-12  col-md-5   neon-div order-2 order-md-1" id="left"> neon-div
                    <Register/>
                </div>
                <div className=" col-12 col-md-5 order-1 order-md-2" id="right" >
                    <img
                        src="picture1.jpg"
                        alt="ping pong paddles"
                        className="img-fluid full-img "
                    />
                </div>
            </div>
        </div>

    );
};


const Log = () => {
    return (
        <div className="container">

            {/*<div className="  row justify-content-center align-items-center vh-100 row-equal-height">*/}

            {/*    <div className="col-md-4 " id="left">*/}
            {/*        <Register/>*/}
            {/*    </div>*/}
            {/*    <div className="col-md-4  " id="right">*/}

            {/*        sdafasdfadsfadsfadsfa*/}
            {/*        /!*<img*!/*/}
            {/*        /!*    src={"pingpong.jpg"}*!/*/}
            {/*        /!*    alt="ping pong paddles"*!/*/}
            {/*        /!*    className="img-fluid  "*!/*/}
            {/*        /!*//*/}
            {/*    </div>*/}
            {/*</div>*/}


            <div className="row  justify-content-center row-equal-height">
                <div className="col-md-4  neon-div-2 " id="left">
                    <LogIn/>
                </div>
                <div className="col-md-4" id="right" >
                    <img
                        src="picture2.jpg"
                        alt="ping pong paddles"
                        className="img-fluid full-img "
                    />
                </div>
            </div>
        </div>

    );
};
 const GPT=()=>{
     return (
         <div className="neon-div">
             Your content here
         </div>

     )
 }


export {LogIn, Register, Reg, Log,GPT}