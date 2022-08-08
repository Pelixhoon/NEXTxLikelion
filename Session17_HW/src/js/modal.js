// 📁 modal.js
// 모달 관련 함수들을 정의하고 내보낸다.
const $ = (selector) => document.querySelector(selector);
const body = $("body");
const modal = $(".modal-container");
const modal2 = $(".modal-container2");

//모달을 여는 함수
const openModal = () => {
  modal.classList.add("open");
  body.style.overflow = "hidden";
};

//모달을 닫는 함수
const closeModal = () => {
  modal.classList.remove("open");
  body.style.overflow = "auto";
};

//모달을 여는 함수
const openModal2 = () => {
  modal2.classList.add("open");
  body.style.overflow = "hidden";
};

//모달을 닫는 함수
const closeModal2 = () => {
  modal2.classList.remove("open");
  body.style.overflow = "auto";
};

export { openModal, closeModal };
export { openModal2, closeModal2 };