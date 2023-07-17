#!/usr/bin/python3
"""Contains test class for commandline program"""


import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand as hbnb
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Defines tests for the command line interpreter"""
    def test_EOF(self):
        """tests the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            result = hbnb().do_EOF('')
            self.assertTrue(result)
            self.assertEqual("", f.getvalue().strip())
            result2 = hbnb().onecmd("EOF")
            self.assertEqual("", f.getvalue().strip())
            self.assertTrue(result2)

    def test_quit(self):
        """tests the quit command"""
        # exit system call made
        with self.assertRaises(SystemExit):
            hbnb().onecmd("quit")

    def test_help(self):
        """tests the help command"""
        # all commands documented
        # EOF  all  create  destroy  help  quit  show  update
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("EOF", output)
            self.assertIn("all", output)
            self.assertIn("create", output)
            self.assertIn("destroy", output)
            self.assertIn("help", output)
            self.assertIn("quit", output)
            self.assertIn("show", output)
            self.assertIn("update", output)

    def test_emptyline(self):
        """tests the emptyline handler"""
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("BaseModel.count()")
            f.truncate(0)
            hbnb().onecmd("")
            hbnb().onecmd("")
            hbnb().onecmd("")
            output = f.getvalue().strip()
            self.assertEqual("", output)

    def test_create(self):
        """tests create command"""
        # missing class name
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create")
            expected = "** class name missing **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # Unsupported class
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create MyModel")
            expected = "** class doesn't exist **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # creates class and returns correct id
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create BaseModel")
            ids = self.get_ids()
            obj_id = f.getvalue().strip()
            self.assertIn(obj_id, ids)

        # create a BaseModel
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create BaseModel")
            hbnb().onecmd("BaseModel.count()")
            expected = "{}".format(self.count_objs('BaseModel'))
            actual = f.getvalue().strip()[-1]
            self.assertEqual(expected, actual)

    def test_show(self):
        """tests show command"""
        # missing class name
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("show")
            expected = "** class name missing **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # Unsupported class
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("show MyModel")
            expected = "** class doesn't exist **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # Supported class, id missing
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("show User")
            expected = "** instance id missing **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # Supported class, invalid id or no such instance
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("show User 1212121212")
            expected = "** no instance found **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # supported class, correct id
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create User")
            user_id = f.getvalue().strip()
            f.truncate(0)
            show_command = "show User {}".format(user_id)
            hbnb().onecmd(show_command)
            output = f.getvalue().strip()
            self.assertEqual(2, output.count(user_id))

    def test_destroy(self):
        """tests destroy command"""
        # missing class name
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("destroy")
            expected = "** class name missing **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # Unsupported class
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("destroy MyModel")
            expected = "** class doesn't exist **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # Supported class, id missing
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("destroy City")
            expected = "** instance id missing **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # Supported class, invalid id or no such instance
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("destroy City 1212121212")
            expected = "** no instance found **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # supported class, correct id
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create City")
            city_id = f.getvalue().strip()
            f.truncate(0)
            ids = self.get_ids()
            self.assertIn(city_id, ids)  # object present in storage
            destroy_command = "destroy City {}".format(city_id)
            hbnb().onecmd(destroy_command)
            ids = self.get_ids()
            self.assertNotIn(city_id, ids)  # destroyed object not in storage
            show_command = "show City {}".format(city_id)
            hbnb().onecmd(show_command)
            expected = "** no instance found **"
            output = f.getvalue().strip()
            self.assertIn(expected, output)

    def test_all(self):
        """tests all command"""
        # all
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("all")
            output = f.getvalue().strip()
            ids = self.get_ids()
            if len(ids) == 0:
                self.assertEqual('[]', output)
            else:
                for i in ids:
                    self.assertIn(i, output)

        # all Unknown class
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("all DummyModel")
            actual = f.getvalue().strip()
            expected = "** class doesn't exist **"
            self.assertEqual(expected, actual)

        # all State
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create State")
            hbnb().onecmd("create State")
            f.truncate(0)
            state_ids = self.get_ids_by_class('State')
            all_ids = self.get_ids()
            non_state_ids = [i for i in all_ids if i not in state_ids]
            hbnb().onecmd("all State")
            output = f.getvalue().strip()
            for state_id in state_ids:
                self.assertIn(state_id, output)
            for other_id in non_state_ids:
                self.assertNotIn(other_id, output)

    def test_update(self):
        """tests update command"""
        # missing class name
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("update")
            expected = "** class name missing **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # Unsupported class
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("update MyModel")
            expected = "** class doesn't exist **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # Supported class, id missing
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("update User")
            expected = "** instance id missing **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # Supported class, invalid id or no such instance
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("update User 1212121212")
            expected = "** no instance found **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

        # Supported class, existing id
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create User")
            user_id = f.getvalue().strip()
            update_command = "update User {}".format(user_id)
            hbnb().onecmd(update_command)
            actual = f.getvalue().strip().split("\n")[1]
            expected = "** attribute name missing **"
            self.assertEqual(expected, actual)

        # Supported class, existing id, attribute
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create User")
            user_id = f.getvalue().strip()
            update_command = "update User {} first_name".format(user_id)
            hbnb().onecmd(update_command)
            actual = f.getvalue().strip().split("\n")[1]
            expected = "** value missing **"
            self.assertEqual(expected, actual)

        # Supported class, existing id, attribute, value
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create User")
            user_id = f.getvalue().strip()
            update_command = "update User {} first_name Betty".format(user_id)
            hbnb().onecmd(update_command)
            show_command = "show User {}".format(user_id)
            hbnb().onecmd(show_command)
            output = f.getvalue().strip()
            self.assertIn("first_name", output)
            self.assertIn("Betty", output)
            self.assertIn("'first_name': 'Betty'", output)

        # Supported class, existing id, attribute, value, extra values
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create User")
            user_id = f.getvalue().strip()
            update_command = "update User {} first_name Betty email \
                    'hbnb@mail.io'".format(user_id)
            hbnb().onecmd(update_command)
            show_command = "show User {}".format(user_id)
            hbnb().onecmd(show_command)
            output = f.getvalue().strip()
            self.assertIn("first_name", output)
            self.assertIn("Betty", output)
            self.assertIn("'first_name': 'Betty'", output)
            self.assertNotIn("email", output)
            self.assertNotIn("hbnb@mail.io", output)

    def test_class_all_function_call(self):
        """tests the <class name>.all() function call"""
        # test State.all()
        with patch('sys.stdout', new=StringIO()) as f:
            state_ids = self.get_ids_by_class('State')
            all_ids = self.get_ids()
            non_state_ids = [i for i in all_ids if i not in state_ids]
            hbnb().onecmd("State.all()")
            output = f.getvalue().strip()
            for state_id in state_ids:
                self.assertIn(state_id, output)
            for other_id in non_state_ids:
                self.assertNotIn(other_id, output)

        # test BaseModel.all()
        with patch('sys.stdout', new=StringIO()) as f:
            bm_ids = self.get_ids_by_class('BaseModel')
            all_ids = self.get_ids()
            non_bm_ids = [i for i in all_ids if i not in bm_ids]
            hbnb().onecmd("BaseModel.all()")
            output = f.getvalue().strip()
            for bm_id in bm_ids:
                self.assertIn(bm_id, output)
            for other_id in non_bm_ids:
                self.assertNotIn(other_id, output)

        # test unknown class
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("MyModel.all()")
            output = f.getvalue().strip()
            expected = "*** Unknown syntax: MyModel.all()"
            self.assertEqual(expected, output)

    def test_class_count_function_call(self):
        """tests the <class name>.count() function call"""
        # Count Amenity instances
        with patch('sys.stdout', new=StringIO()) as f:
            a_count = self.count_objs('Amenity')
            hbnb().onecmd("Amenity.count()")
            count = f.getvalue().strip()
            self.assertEqual(f"{a_count}", count)
            hbnb().onecmd("create Amenity")
            hbnb().onecmd("Amenity.count()")
            new_count = f.getvalue().strip().split("\n")[-1]
            diff = int(new_count) - int(count)
            self.assertEqual(diff, 1)

    def test_class_show_function_call(self):
        """tests the <class name>.show(<id>) function call"""
        # supported class, correct id
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create Place")
            place_id = f.getvalue().strip()
            show_command = "Place.show('{}')".format(place_id)
            hbnb().onecmd(show_command)
            output = f.getvalue().strip()
            self.assertEqual(3, output.count(place_id))

        # supported class, non-existent id
        with patch('sys.stdout', new=StringIO()) as f:
            show_command = "Place.show('121212121')"
            hbnb().onecmd(show_command)
            output = f.getvalue().strip()
            expected = "** no instance found **"
            self.assertEqual(expected, output)

    def test_class_destroy_function_call(self):
        """tests the <class name>.destroy(<id>) function call"""
        # supported class, correct id
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create Review")
            review_id = f.getvalue().strip()
            f.truncate(0)
            ids = self.get_ids()
            self.assertIn(review_id, ids)  # object present in storage
            destroy_command = "Review.destroy('{}')".format(review_id)
            hbnb().onecmd(destroy_command)
            ids = self.get_ids()
            self.assertNotIn(review_id, ids)  # destroyed object not in storage
            hbnb().onecmd(destroy_command)  # attempt delete on destroyed obj
            expected = "** no instance found **"
            output = f.getvalue().strip()
            self.assertIn(expected, output)

        # Supported class, invalid id or no such instance
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("City.destroy('1212121212')")
            expected = "** no instance found **"
            actual = f.getvalue().strip()
            self.assertEqual(expected, actual)

    def test_class_update_with_key_value_function_call(self):
        """tests <class name>.update(<id>, <attribute name>, <attribute value>)
        function call
        """
        # Supported class, existing id, attribute, value
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create User")
            user_id = f.getvalue().strip()
            show_command = "show User {}".format(user_id)
            output = f.getvalue().strip()
            self.assertNotIn("first_name", output)
            self.assertNotIn("John", output)
            update_command = "User.update('{}', 'first_name', 'John')"\
                .format(user_id)
            hbnb().onecmd(update_command)
            hbnb().onecmd(show_command)
            output = f.getvalue().strip()
            self.assertIn("first_name", output)
            self.assertIn("John", output)
            self.assertIn("'first_name': 'John'", output)
            self.assertNotIn("'age' : '89'", output)
            update_command = "User.update('{}', 'age', 89)".format(user_id)
            hbnb().onecmd(update_command)
            hbnb().onecmd(show_command)
            output = f.getvalue().strip()
            self.assertIn("'age': '89'", output)

    def test_class_update_with_dictionary_function_call(self):
        """tests the <class name>.update(<id>, <dictionary representation>)
        function call
        """
        # Supported class, existing id, dictionary representation
        with patch('sys.stdout', new=StringIO()) as f:
            hbnb().onecmd("create User")
            user_id = f.getvalue().strip()
            show_command = "show User {}".format(user_id)
            output = f.getvalue().strip()
            self.assertNotIn("'f_name': 'John'", output)
            self.assertNotIn("'age' : '89'", output)
            update_dict = "{'f_name': 'John', 'age': 89}"
            u_cmd = f"User.update('{user_id}', {update_dict})"
            hbnb().onecmd(u_cmd)
            hbnb().onecmd(show_command)
            output = f.getvalue().strip()
            self.assertIn("'f_name': 'John'", output)
            self.assertIn("'age': '89'", output)

    # Helper methods for HBNBCommand commands #
    def count_objs(self, cls_name):
        """counts the actual objects of type 'cls_name'0 present in storage"""
        all_objs = storage.all()
        count = 0
        for k, v in all_objs.items():
            if v["__class__"] == cls_name:
                count += 1
        return count

    def get_ids(self):
        """returns a list of ids of current objects in storage"""
        all_objs = storage.all()
        ids = []
        for k, v in all_objs.items():
            ids.append(v["id"])
        return ids

    def get_ids_by_class(self, cls_name):
        """returns list of ids of the specified class"""
        all_objs = storage.all()
        ids = []
        for k, v in all_objs.items():
            if v["__class__"] == cls_name:
                ids.append(v["id"])
        return ids


if __name__ == "__main__":
    unittest.main()
