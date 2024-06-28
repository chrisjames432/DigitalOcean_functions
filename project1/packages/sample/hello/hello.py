def main(args):
      name = args.get("name", "stranger")
      greeting = "Hi how are you doing  " + name + "!"
      print(greeting)
      return {"body": greeting}
