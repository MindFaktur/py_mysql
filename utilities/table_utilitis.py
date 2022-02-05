import pymysql


class TableUtilities:

    def get_input(self, value_to_get):
        """
        Get user input for the given parameter name.
        :param value_to_get: data to get.
        :return:user input.
        """
        try:
            value = input(f"Please enter {value_to_get} ")
            if value.isdigit():
                print("Please enter a string value")
                return self.get_input(value_to_get)
            else:
                return value
        except Exception:
            print(f"Exception at get_input: {value_to_get}")
