import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.stereotype.*;
import org.springframework.web.bind.annotation.*;

@RestController
@EnableAutoConfiguration
public class HelloOnefactor {

    @RequestMapping("/")
    String home() {
        return "Hello OneFactor v 0.0.2 !";
    }

    public static void main(String[] args) throws Exception {
        SpringApplication.run(HelloOnefactor.class, args);
    }

}
