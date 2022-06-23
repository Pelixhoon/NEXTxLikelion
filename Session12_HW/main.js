function play(e) {
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
  const key = document.querySelector(`li[data-key="${e.keyCode}"]`);
  // 1. audio 변수를 html에서 select해주세요. audio변수는 누르는 키보드에 헤당하는 keycode를 가지고 있는 음악파일입니다.
  // 2. key 변수를 html에서 select해주세요. key 변수는 누르는 키보드에 헤당하는 keycode를 가진 li 태그입니다.
  if (audio) {
    audio.play();
    key.classList.add('play');
  };
};

function pause(e){
  // 1. audio 변수를 html에서 select해주세요. audio변수는 누르는 키보드에 헤당하는 keycode를 가지고 있는 음악파일입니다.
  // 2. key 변수를 html에서 select해주세요. key 변수는 누르는 키보드에 헤당하는 keycode를 가진 li 태그입니다.
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
  const key = document.querySelector(`li[data-key="${e.keyCode}"]`);
  if (audio) {
    audio.currentTime = 0;
    audio.pause();
    key.classList.remove('play');
    //    3. 누른 key에 play 클래스를 제거하세요
  }
};

// 4. 키보드를 눌렀을때 play함수가 실행되게, 키보드를 뗀다면 pause함수가 실행되게 해주세요

document.addEventListener('keydown',play);
document.addEventListener('keyup',pause);