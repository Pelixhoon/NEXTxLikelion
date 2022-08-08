// 📁 cookie.js
// 쿠키 관련 함수들을 저장하고 내보낸다.

// 만료기한을 정해 쿠키 생성하기
const setCookie = (name, value, expireDays) => {
  // 현재 날짜와 시간이 저장된 Date 객체 생성하기
  let today = new Date();
  // 오늘 날짜에 expireDays만큼 더해서 만료시간을 구하기
  today.setDate(today.getDate() + expireDays);
  // 쿠키 생성하기 (템플릿 리터럴 활용)
  document.cookie = 
  `${name}=${value};expires=${today.toGMTString()}`;
};

// 특정 이름의 쿠키를 가져오기
const getCookie = (name) => {
  // 로컬에 저장된 모든 쿠키 읽어오기
  let cookie = document.cookie;
  // 로컬에 저장된 쿠키가 존재하면 쿠키를 배열에 저장
  //배열을 순회하며 내가 원하는 이름의 쿠키를 리턴하기
  if (document.cookie) {
    // 배열을 순회하면서 쿠키의 name에 대한 value값을 리턴 (반복문)
    let cookieArray = cookie.split("; ");
    for (let index in cookieArray) {
      let cookieName = cookieArray[index].split("=");
      if (cookieName[0] == name) {
        return cookieName[1];
      }
    }
  }
  return;
};

export { setCookie, getCookie };