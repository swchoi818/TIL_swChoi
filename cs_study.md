# Google 검색창에 `naver.com` 입력 시 동작 과정

## 1. 개요
사용자가 **Google 검색창**에 `naver.com`을 입력하고 Enter를 누르면 다음 단계들이 순차적으로 일어난다.

1. 브라우저 입력 이벤트 처리  
2. Google 검색 URL 생성  
3. DNS 조회 및 네트워크 연결 (TCP, TLS)  
4. Google 서버에서 검색 처리  
5. HTTP 응답 → 브라우저 렌더링  

---

## 2. 상세 동작 과정

### 2.1 사용자 입력 및 요청 생성
- 사용자가 Google 검색창에 `naver.com` 입력
- JavaScript 이벤트 감지 후 **검색 요청 URL** 생성

https://www.google.com/search?q=naver.com

yaml
복사

---

### 2.2 네트워크 요청 전송 (HTTPS 기반)

#### OSI 7계층 흐름

| 계층 | 역할 |
|------|------|
| 7 응용계층 | HTTP 요청 생성 (`GET /search?q=naver.com`) |
| 6 표현계층 | TLS 암호화 처리 |
| 5 세션계층 | TLS 세션 관리 |
| 4 전송계층 | TCP 연결 및 세그먼트 분할 |
| 3 네트워크계층 | IP 주소 기반 라우팅 |
| 2 데이터링크계층 | 이더넷/와이파이 프레임 전송 |
| 1 물리계층 | 전기/광 신호 전송 |

---

## 3. 패킷 단위 동작

### 3.1 DNS 조회
- 브라우저는 `www.google.com`의 IP 주소를 모르므로 DNS 질의 수행
- UDP 기반으로 DNS 서버에 요청 전송

[클라이언트] → [로컬 DNS 서버]
요청: www.google.com → ?
응답: 142.250.xxx.xxx

yaml
복사

---

### 3.2 TCP 3-way Handshake

클라이언트 → 서버: SYN

서버 → 클라이언트: SYN-ACK

클라이언트 → 서버: ACK

yaml
복사

- 이 과정으로 TCP 연결이 확립됨

---

### 3.3 TLS Handshake (HTTPS 암호화)

- TLS 버전 협상
- 인증서 교환 (서버 공개키 포함)
- 키 교환 (예: ECDHE)
- 세션 키 설정 → 이후 트래픽 암호화됨

---

### 3.4 HTTP 요청 전송

암호화된 HTTP GET 요청 예시:

GET /search?q=naver.com HTTP/1.1
Host: www.google.com
User-Agent: Chrome/...

yaml
복사

---

## 4. Google 서버 검색 처리

- 입력된 쿼리 `naver.com` 파싱
- 검색 인덱스 조회 및 랭킹 알고리즘 적용
- 결과 HTML 페이지 생성
- HTTPS로 응답 전송

---

## 5. 브라우저 렌더링 과정

1. TLS 복호화
2. HTML 파싱 → DOM 트리 생성
3. CSS 파싱 → 렌더 트리 생성
4. JS 실행 (동적 요소 처리)
5. 최종 화면 렌더링

---

## 6. 네트워크 흐름도 (텍스트 다이어그램)

[User types naver.com in Google Search bar]
↓
[Browser JS triggers GET /search?q=naver.com]
↓
[DNS Request] ──▶ [DNS 서버] ──▶ [Google IP 반환]
↓
[TCP SYN] ──▶ [Google 서버]
[ SYN-ACK] ◀──
[ ACK] ──▶
↓
[TLS Handshake → 세션 암호화 설정]
↓
[HTTP GET 요청 전송 (암호화됨)]
↓
[Google 서버 검색 처리 및 HTML 응답]
↓
[Browser 렌더링 → 사용자 화면 표시]

yaml
복사

---

## 7. 추가 고려 사항

- 주소창(URL bar)에 `naver.com` 입력 시:
  - DNS 조회 후 **직접 네이버 서버에 접속**
  - Google 검색 과정 없음

- 검색창에 입력한 경우:
  - **Google 서버**에서 쿼리로 처리 → 검색 결과 페이지 표시
