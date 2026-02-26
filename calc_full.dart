import 'package:flutter/material.dart';
import 'dart:math';   // for pow and e

void main(){
  runApp(MyApp());
}

class MyApp extends StatefulWidget{
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp>{
  TextEditingController n1=TextEditingController();
  TextEditingController n2=TextEditingController();
  String result ="";

  void add(){
    double a = double.parse(n1.text);
    double b = double.parse(n2.text);
    setState(() {
      result = (a+b).toString();
    });
  }

  void sub(){
    double a = double.parse(n1.text);
    double b = double.parse(n2.text);
    setState(() {
      result = (a-b).toString();
    });
  }

  void mul(){
    double a = double.parse(n1.text);
    double b = double.parse(n2.text);
    setState(() {
      result = (a*b).toString();
    });
  }

  void div(){
    double a = double.parse(n1.text);
    double b = double.parse(n2.text);
    setState(() {
      result = (a/b).toString();
    });
  }

  // Power a^b
  void power(){
    double a = double.parse(n1.text);
    double b = double.parse(n2.text);
    setState(() {
      result = pow(a,b).toString();
    });
  }

  // e^a
  void epower(){
    double a = double.parse(n1.text);
    setState(() {
      result = pow(e,a).toString();
    });
  }

  Widget build (BuildContext context){
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text("Calculator"),),
        body: Padding(
          padding: EdgeInsets.all(20),
          child: Column(
            children: [
              TextField(controller: n1,
                  decoration: InputDecoration(labelText: "Number1")),
              TextField(controller: n2,
                  decoration: InputDecoration(labelText: "Number2")),

              Row(   // All buttons in same row
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  ElevatedButton(onPressed: add, child: Text("+")),
                  ElevatedButton(onPressed: sub, child: Text("-")),
                  ElevatedButton(onPressed: mul, child: Text("*")),
                  ElevatedButton(onPressed: div, child: Text("/")),
                  ElevatedButton(onPressed: power, child: Text("a^b")),
                  ElevatedButton(onPressed: epower, child: Text("e^x")),
                ],
              ),

              SizedBox(height: 20),
              Text("Result :  $result",
                  style: TextStyle(fontSize: 20)),
            ],
          ),
        ),
      ),
    );
  }
}
