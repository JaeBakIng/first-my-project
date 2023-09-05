var cnt=0 //카운터 초기화
        var p_1=document.getElementById("p_1") //id가 p_1 태그의 모든 속성 메소드 가져와서 p_1이라는 변수에 넣음
        function ff() {
            cnt++;
            p_1.innerHTML= cnt +'번 클릭됨'//p_1의 변수를 HTML로써 씀

            if(cnt%2==0){ //클릭횟수 짝수
                document.body.style.backgroundColor='pink'
            }
            else{//클릭횟수 홀수
                document.body.style.backgroundColor='gold'
            }
        }