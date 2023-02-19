import cmd
import os
import uuid

class Hello(cmd.Cmd, object):
    """
    SIMPLE GREETINGS
    """
    FRIENDS = ['Ayomide', 'Samuel', 'James', 'Angela', 'Jenny', "Abike"]
    last_output = ''
    def do_greet(self, person):
        """ SIMPLE GREETINGS
        Greet the [person]
        """
        if person and person in self.FRIENDS:
            greeting = 'hi %s!' % person
        elif person:
            greeting = 'Hello ' + person
        else:
            greeting = 'Hello'
        print(greeting)

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [f for f in self.FRIENDS if f.startswith(text)]
        return completions
    def do_shell(self,line):
        print(f"Runnig shell command: {line}")
        output = os.popen(line).read()
        print(output)
        self.last_output = output

    def do_echo(self, line):
        "Print the input, replacing $out with the output of the input "

        print(line.replace('$out', self.last_output))

    def help_shell(self):
        print("Execute any shell command.")

    def help_greet(self):

        print('\n'.join(
            ['greet [person]',
             'Greet the named person']
        ))

    def postloop(self):
        print

    def do_EOF(self, line):
        """

        :param line: EXIT THE SHELL
        :return: TRUE
        """
        ask = input("Do you want ot exit? Y or N ").upper()
        if ask == "Y":
            return True



if __name__ == "__main__":
    Hello().cmdloop()


user_id = uuid.uuid3(uuid.NAMESPACE_DNS, "owoyemi idris")

print(user_id)

owoyemi = "00e8a5ec-99dc-3d8e-995a-489073983ce2"