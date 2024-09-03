import { userForm } from "./getUser.js";
const windowDiv = document.querySelector(".window");

const sideBar = document.createElement("div");
sideBar.className = "sideBar";

const mainBar = document.createElement("div");
mainBar.className = "mainBar";


mainBar.appendChild(userForm);

windowDiv.appendChild(sideBar);
windowDiv.appendChild(mainBar);

export {mainBar}
