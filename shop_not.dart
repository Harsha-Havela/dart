import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

void main() => runApp(MyApp());
final plugin = FlutterLocalNotificationsPlugin();

class MyApp extends StatefulWidget {
  @override State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  Map<String,int> items = {"Shoes":1000,"Bag":500,"Watch":1500};
  Map<String,int> cart = {};
  int total = 0;

  @override
  void initState() {
    super.initState();
    plugin.initialize(const InitializationSettings(
      android: AndroidInitializationSettings('@mipmap/ic_launcher')));
  }

  void add(String name,int price){
    setState(() {
      cart[name] = (cart[name] ?? 0) + 1;
      total += price;
    });
  }

  void cancel(String name,int price){
    if(cart.containsKey(name) && cart[name]! > 0){
      setState(() {
        cart[name] = cart[name]! - 1;
        total -= price;
        if(cart[name]==0) cart.remove(name);
      });
    }
  }

  String cartDisplay(){
    if(cart.isEmpty) return "Cart is Empty";
    return cart.entries
        .map((e)=> "${e.key} (${e.value})")
        .join(", ");
  }

  void showTotal() async => await plugin.show(
    0,"Final Bill","Total Amount: ₹$total",
    const NotificationDetails(
      android: AndroidNotificationDetails(
        "id","name",importance: Importance.max,priority: Priority.high)));

  @override
  Widget build(BuildContext c) => MaterialApp(
    debugShowCheckedModeBanner:false,
    home: Scaffold(
      appBar: AppBar(title: Text("Shopping App"),backgroundColor: Colors.teal),
      body: Column(children: [
        Expanded(child: ListView(
          children: items.entries.map((e)=>Card(
            child: ListTile(
              title: Text("${e.key} - ₹${e.value}"),
              trailing: Row(mainAxisSize: MainAxisSize.min, children: [
                ElevatedButton(
                  onPressed: ()=>add(e.key,e.value), child: Text("Add")),
                SizedBox(width:5),
                ElevatedButton(
                  onPressed: ()=>cancel(e.key,e.value), child: Text("Cancel")),
              ]),
            ))).toList())),

        Container(
          padding: EdgeInsets.all(15),
          color: Colors.teal,
          width: double.infinity,
          child: Text(
            "${cartDisplay()}\nTotal: ₹$total",
            style: TextStyle(color: Colors.white,fontSize:16),
            textAlign: TextAlign.center),
        ),

        ElevatedButton(onPressed: showTotal, child: Text("Show Total")),
      ]),
    ),
  );
}
