import 'package:flutter/material.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      title: "Shopping Application",
      home: ShoppingScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class ShoppingScreen extends StatefulWidget{
  @override
  _ShoppingScreenState createState() => _ShoppingScreenState();

}

class _ShoppingScreenState extends State<ShoppingScreen>{

  int apple=0;
  int banana=0;
  int orange=0;

  int apple_price=120;
  int banana_price=80;
  int orange_price=90;

  void increaseApple(){
    setState(() {
      apple++;
    });
  }

  void increaseBanana(){
    setState(() {
      banana++;
    });
  }

  void increaseOrange(){
    setState(() {
      orange++;
    });
  }

  void decreaseApple(){
    setState(() {
      apple--;
    });
  }

  void decreaseBanana(){
    setState(() {
      banana--;
    });
  }

  void decreaseOrange(){
    setState(() {
      orange--;
    });
  }

  void showNotification(String message){
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content:Text(message))
    );
  }
  int total(){
    return ( (apple*apple_price)+(banana*banana_price)+(orange*orange_price));
  }

  Widget build(BuildContext context){
    return Scaffold(
      backgroundColor: Colors.white,

      appBar: AppBar(
        title: Text("Shopping Application"),
        backgroundColor: Colors.lightBlue,
        centerTitle: true,
      ),

      body:Column(
        children: [
          Container(
            margin: EdgeInsets.all(20),
            padding:EdgeInsets.all(20),
            color: Colors.lightBlue,
            child:Column(
              children: [
                Image.asset(
                  "assets/apple.jpg",
                  height: 120,
                ),
                Text("Apple"),
                Text("Rs.120 per kg"),
                Text("$apple kg"),

                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    ElevatedButton(onPressed:increaseApple, child: Text("+")),
                    ElevatedButton(onPressed:decreaseApple, child: Text("-")),
                  ],
                ),
                ElevatedButton(
                    onPressed:() {
                      showNotification("Apple Added");
                    },
                    child: Text("Click")
                ),
              ],
            )
          ),
          SizedBox(height: 20),
          Container(
              margin: EdgeInsets.all(20),
              padding:EdgeInsets.all(20),
              color: Colors.lightBlue,
              child:Column(
                children: [
                  Text("Banana"),
                  Text("Rs.80 per kg"),
                  Text("$banana kg"),

                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      ElevatedButton(onPressed:increaseBanana, child: Text("+")),
                      ElevatedButton(onPressed:decreaseBanana, child: Text("-")),
                    ],
                  )
                ],
              )
          ),
          SizedBox(height: 20),

          Container(
              margin: EdgeInsets.all(20),
              padding:EdgeInsets.all(20),
              color: Colors.lightBlue,
              child:Column(
                children: [
                  Text("Orange"),
                  Text("Rs.90 per kg"),
                  Text("$orange kg"),

                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      ElevatedButton(onPressed:increaseOrange, child: Text("+")),
                      ElevatedButton(onPressed:decreaseOrange, child: Text("-")),
                    ],
                  )
                ],
              )
          ),

          SizedBox(height: 20),

          Text(
            "Total:${total()}",
            style: TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      )
    );
  }


}


#2

  import 'package:flutter/material.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      title: "Shopping Application",
      home: ShoppingScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class ShoppingScreen extends StatefulWidget{
  @override
  _ShoppingScreenState createState() => _ShoppingScreenState();

}

class _ShoppingScreenState extends State<ShoppingScreen>{

  int apple=0;
  int banana=0;
  int orange=0;

  int apple_price=120;
  int banana_price=80;
  int orange_price=90;

  void increaseApple(){
    setState(() {
      apple++;
    });
  }

  void increaseBanana(){
    setState(() {
      banana++;
    });
  }

  void increaseOrange(){
    setState(() {
      orange++;
    });
  }

  void decreaseApple(){
    setState(() {
      apple--;
    });
  }

  void decreaseBanana(){
    setState(() {
      banana--;
    });
  }

  void decreaseOrange(){
    setState(() {
      orange--;
    });
  }

  void showNotification(String message){
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content:Text(message))
    );
  }
  int total(){
    return ( (apple*apple_price)+(banana*banana_price)+(orange*orange_price));
  }

  Widget build(BuildContext context){
    return Scaffold(
      backgroundColor: Colors.white,

      appBar: AppBar(
        title: Text("Shopping Application"),
        backgroundColor: Colors.lightBlue,
        centerTitle: true,
      ),

      body:Column(
        children: [
          Container(
            margin: EdgeInsets.all(20),
            padding:EdgeInsets.all(20),
            color: Colors.lightBlue,
            child:Column(
              children: [
                Image.asset(
                  "assets/apple.jpg",
                  height: 120,
                ),
                Text("Apple"),
                Text("Rs.120 per kg"),
                Text("$apple kg"),

                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    ElevatedButton(onPressed:increaseApple, child: Text("+")),
                    ElevatedButton(onPressed:decreaseApple, child: Text("-")),
                  ],
                ),
                ElevatedButton(
                    onPressed:() {
                      showNotification("Apple Added");
                    },
                    child: Text("Click")
                ),
              ],
            )
          ),
          SizedBox(height: 20),
          Container(
              margin: EdgeInsets.all(20),
              padding:EdgeInsets.all(20),
              color: Colors.lightBlue,
              child:Column(
                children: [
                  Text("Banana"),
                  Text("Rs.80 per kg"),
                  Text("$banana kg"),

                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      ElevatedButton(onPressed:increaseBanana, child: Text("+")),
                      ElevatedButton(onPressed:decreaseBanana, child: Text("-")),
                    ],
                  )
                ],
              )
          ),
          SizedBox(height: 20),

          Container(
              margin: EdgeInsets.all(20),
              padding:EdgeInsets.all(20),
              color: Colors.lightBlue,
              child:Column(
                children: [
                  Text("Orange"),
                  Text("Rs.90 per kg"),
                  Text("$orange kg"),

                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      ElevatedButton(onPressed:increaseOrange, child: Text("+")),
                      ElevatedButton(onPressed:decreaseOrange, child: Text("-")),
                    ],
                  )
                ],
              )
          ),

          SizedBox(height: 20),

          Text(
            "Total:${total()}",
            style: TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      )
    );
  }


}

#3

  import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MaterialApp(
      title: "Http request",
      home: HomeScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class HomeScreen extends StatefulWidget{
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen>{

  String data="No data";

  void fetchdata() async{
    var url=Uri.parse("https://jsonplaceholder.typicode.com/posts/1");
    var response= await http.get(url);

    setState(() {
      data=response.body;
    });
  }

  Widget build(BuildContext context){
    return Scaffold(
      backgroundColor: Colors.white,

      appBar: AppBar(
        title: Text("Http Request"),
        backgroundColor: Colors.lightBlue,
      ),

      body: Padding(
          padding: EdgeInsets.all(20),
        child: Center(
          child: Column(
            children: [

              Text(
                data,
                style: TextStyle(fontSize: 16),
              ),

              ElevatedButton(
                  onPressed:fetchdata,
                  child: Text("Fetch data")
              )
            ],
          ),
        ),
      ),
    );
  }
}

#4

  import 'package:flutter/material.dart';
import 'dart:math';

void main() {
  runApp(MyApp());
}

// ROOT
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Number Game',
      home: GameScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

// STATEFUL
class GameScreen extends StatefulWidget {
  @override
  _GameScreenState createState() => _GameScreenState();
}

class _GameScreenState extends State<GameScreen> {

  int number = 0;
  int score = 0;
  String message = "Press Start";

  // GENERATE NUMBER
  void startGame() {
    setState(() {
      number = Random().nextInt(10); // 0 to 9
      message = "Is it Even?";
    });
  }

  // CHECK EVEN
  void checkEven() {
    setState(() {
      if (number % 2 == 0) {
        score++;
        message = "Correct!";
      } else {
        message = "Wrong!";
      }
    });
  }

  // CHECK ODD
  void checkOdd() {
    setState(() {
      if (number % 2 != 0) {
        score++;
        message = "Correct!";
      } else {
        message = "Wrong!";
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[200],

      appBar: AppBar(
        title: Text("Number Game"),
        backgroundColor: Colors.blue,
      ),

      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [

          // NUMBER DISPLAY
          Text(
            "$number",
            style: TextStyle(fontSize: 40),
          ),

          SizedBox(height: 20),

          Text(
            message,
            style: TextStyle(fontSize: 20),
          ),

          SizedBox(height: 20),

          // BUTTONS
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              ElevatedButton(
                onPressed: checkEven,
                child: Text("Even"),
              ),
              ElevatedButton(
                onPressed: checkOdd,
                child: Text("Odd"),
              ),
            ],
          ),

          SizedBox(height: 20),

          ElevatedButton(
            onPressed: startGame,
            child: Text("Start"),
          ),

          SizedBox(height: 20),

          // SCORE
          Text(
            "Score: $score",
            style: TextStyle(fontSize: 22),
          ),
        ],
      ),
    );
  }
}

#5

  import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: DateApp(),
    );
  }
}

class DateApp extends StatefulWidget {
  @override
  State<DateApp> createState() => _DateAppState();
}

class _DateAppState extends State<DateApp> {
  DateTime? selectedDate;

  void pickDate() async {
    DateTime? picked = await showDatePicker(
      context: context,
      initialDate: DateTime.now(),
      firstDate: DateTime.now(), // ❌ past not allowed
      lastDate: DateTime(2100),
    );

    if (picked != null) {
      setState(() {
        selectedDate = picked;
      });

      checkAlert(picked);
    }
  }

  void checkAlert(DateTime pickedDate) {
    int diff = pickedDate.difference(DateTime.now()).inDays;

    if (diff <= 2) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text("⚠️ Date is within 2 days!"),
          backgroundColor: Colors.red,
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Date Picker")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: pickDate,
              child: Text("Pick Date"),
            ),

            SizedBox(height: 20),

            Text(
              selectedDate == null
                  ? "No date selected"
                  : "Selected: ${selectedDate!.day}/${selectedDate!.month}/${selectedDate!.year}",
              style: TextStyle(fontSize: 18),
            ),
          ],
        ),
      ),
    );
  }
}

dependencies: for http
  math_expressions:^2.4.0
  http:^0.13.6
