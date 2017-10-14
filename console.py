#!/usr/bin/python3
"""Command Interpreter - Console"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand - console for the AirBnB clone
        Note: "help <cmd>" functionality is provided by cmd module
    Usage:
        create [class=BaseModel]
        show [class=BaseModel [id=12234-1234-1234]]
        destroy [class=BaseModel] [id=1234-1234-1234]
        all | all [class=BaseModel]
        update [class=BaseModel] [id=1234-1234-1234] [key] [value]
    """
    # ----- basic AirBnB clone commands -----
    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        raise SystemExit

    def emptyline(self):
        """Do nothing on empty input line
        """
        pass

    # ----- basic Console CRUD commands -----
    def do_create(self, arg):
        """Create BaseModel instance, saves to JSON file, prints ID"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg in models.types:
            obj = models.types[arg]()
            obj.save()
            print(obj.id)
            models.count[obj.__class__.__name__] += 1
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show class object with ID"""
        input = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif len(input) == 1:
            print("** instance id missing **")
            return
        if input[0] in models.types:
            allObjs = models.storage.all()
            realID = input[0] + "." + input[1]
            if realID in allObjs:
                print(allObjs[realID])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy an object"""
        input = arg.split()
        if len(input) == 2:
            realID = input[0] + "." + input[1]
        allObjs = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif len(input) == 1:
            print("** instance id missing **")
            return
        if input[0] in models.types:
            if realID in allObjs:
                allObjs.pop(realID)
                models.count[input[0]] -= 1
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Show all objects"""
        input = arg.split()
        allObjs = models.storage.all()
        str = "["
        if len(arg) == 0:
            for k in allObjs:
                str = str + allObjs[k].__str__() + ', '
            str = str[:-2] + ']'
            print(str)
        elif (len(input) == 1 and input[0] in models.types):
            for k in allObjs:
                if input[0] in k:
                    str = str + allObjs[k].__str__() + ', '
            str = str[:-2] + ']'
            print(str)
        else:
            print("** class doesn't exist **")

    def do_update(self, args, **kwargs):
        """Update obj atribute with info
        """
        if args:
            args = args.split()
            argsize = len(args)
            if argsize >= 2:
                ID = args[0] + "." + args[1]
            else:
                if argsize == 1:
                    print("** instance id missing **")
                elif argsize == 0:
                    print("** class name missing **")
                return
        try:
            d = models.storage.all()[ID].to_dict()
            if kwargs:
                d.update(kwargs)
            else:
                if argsize == 2:
                    print("** attribute name missing **")
                    return
                for i in range(0, argsize, 2):
                    if i >= 2:
                        args[i] = args[i].strip(':')
                        args[i] = args[i].strip('"')
                        try:
                            args[i+1] = args[i+1].strip('"')
                            d[args[i]] = args[i+1]
                        except:
                            print("** value missing **")
                            return
            d.pop("updated_at")
            d.pop("__class__")
            types[args[0]](**d)
        except:
            print("** no instance found **")

    def default(self, line):
        """default behavior method"""
        import re
        import ast
        js = {}
        methods = {'all': self.do_all, 'show': self.do_show,
                   'destroy': self.do_destroy, 'update': self.do_update}
        ln = re.split('[.,()]', line)
        if '{' in line:
            js = ast.literal_eval(re.search('({.+})', line).group(0))
            ln = ln[:3]
        if len(ln) >= 2:
            meth = ln.pop(1)
        else:
            print("*** Unknown syntax:", ln[0])
            return
        if meth == "show" or meth == "update":
            ln[1] = ln[1].strip('"')
        elif meth == "count":
            print(models.count[ln[0]])
            return
        ln = " ".join(ln)
        ln = ln.replace('\'', '"')
        if meth in methods:
            methods[meth](ln, **js)

if __name__ == '__main__':
    console = HBNBCommand()
    console.prompt = "(hbnb) "
    console.cmdloop()
