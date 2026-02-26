import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String msg = "Hello";
  IconData icon = Icons.home;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text("GUI")),
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(icon, size: 50, color: Colors.red),
              Text(msg,
                  style: TextStyle(fontSize: 25, color: Colors.blue)),
              ElevatedButton(
                  onPressed: () => setState(() {
                        msg = "Welcome";
                        icon = Icons.thumb_up;
                      }),
                  child: Text("Button")),
              GestureDetector(
                onTap: () => setState(() {
                  msg = "Tapped";
                  icon = Icons.touch_app;
                }),
                onDoubleTap: () => setState(() {
                  msg = "Double Tap";
                  icon = Icons.favorite;
                }),
                onHorizontalDragEnd: (_) => setState(() {
                  msg = "Swiped";
                  icon = Icons.swipe;
                }),
                child: Container(
                    padding: EdgeInsets.all(10),
                    color: Colors.green,
                    child: Text("Tap Area")),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
