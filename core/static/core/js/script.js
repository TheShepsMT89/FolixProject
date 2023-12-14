//! VARIABLES

const login = document.getElementById("login");
const register = document.getElementById("register");
//
const textoPrincipal = document.getElementById("bienvenida");
//
const btnLogin = document.getElementById("boton");
const btnLogin2 = document.getElementById("boton2");
const btnResponsive = document.getElementById("botonresponsive");
//
const btnRegistro = document.getElementById("registro");
//
const btnTemas = document.getElementById("btnTemas");
const sctTemas = document.getElementById("SeccionTemas");
//
const sctHoja = document.getElementById("SeccionHoja");
const btnRegistrarse = document.getElementById("registrarse");
//
const footer = document.getElementById("seccion2");
//
const mobile = document.getElementById("mobile-menu");

//! FUNCIONES

function AparecerLogin() {
  login.classList.add("scale-up-center");
  login.style.display = "flex";
  register.style.display = "none";
  footer.style.display = "none";
  if (sctHoja !== null) {
    sctHoja.style.display = "none";
  } else if (sctTemas !== null) {
    sctTemas.style.display = "none";
  }
}

function AparecerRegistro() {
  register.classList.add("scale-up-center");
  register.style.display = "flex";
  login.style.display = "none";
}

function DesaparecerElementos() {
  textoPrincipal.classList.remove("miClase");
  textoPrincipal.classList.add("scale-down-blur-center");
  setTimeout(function () {
    textoPrincipal.style.display = "none";
  }, 360);
}

function DesaparecerRegistro() {
  register.classList.add("scale-down-blur-center");
  setTimeout(function () {
    register.style.display = "none";
  }, 360);
}

function DevolucionDeElementos() {
  register.style.display = "none";
  textoPrincipal.classList.add("miClase");
  textoPrincipal.style.display = "block";
  footer.style.display = "flex";
  sctHoja.style.display = "flex";
  sctTemas.style.display = "flex";
}

//! EVENTOS

btnLogin.addEventListener("click", function () {
  if (textoPrincipal !== null) {
    DesaparecerElementos();
  }
  AparecerLogin(login);
});

btnLogin2.addEventListener("click", function () {
  if (textoPrincipal !== null) {
    DesaparecerElementos();
  }
  AparecerLogin(login);
});

btnResponsive.addEventListener("click", function () {
  if (textoPrincipal !== null) {
    DesaparecerElementos();
  }
  AparecerLogin(login);
});

btnRegistro.addEventListener("click", function () {
  if (textoPrincipal !== null) {
    DesaparecerElementos();
  }
  AparecerRegistro(register);
});

btnRegistrarse.addEventListener("click", function () {
  DevolucionDeElementos();
});
