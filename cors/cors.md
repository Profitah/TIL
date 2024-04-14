# CORS

## CORS에러란?
origin 서버가 아닌 다른 서버에서 데이터를 요청했을때 다른 출처 리소스 접근 제한 정책 (SOP 정책) 위반으로 이를 가져올 수 없는 것.

## 해결 방법
(1) 서버 프록시(proxy) 설정<br>
origin 서버에 프록시를 설정한다.<br>
- <br>

* 서버 프록시 : 서버에서 프록시 서버를 구성하고 관리하게 하는 것.<br>
* 프록시 : 클라이언트와 서버 사이에서 중계 역할을 수행하는 컴퓨터 시스템이나 응용 프로그램

```json
{
  "proxy": "http://example.com"
}


```

(2) CORS(cross-origin resource sharing)<br>
서버에 CORS 헤더를 설정하여 클라이언트가 다른 출처의 리소스에 접근할 수 있도록 허용

```java
@Configuration
public class CorsConfiguration implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("http://example.com")
                .allowedOrigins("*");
    }
}
```
(http://example.com으로 시작하는 모든 URL에서  오리진서버로 하는 모든 요청을 허용하는 코드)<br>




참고자료 : https://the1ibrary.com/kr/interview/13/What-is-CORS