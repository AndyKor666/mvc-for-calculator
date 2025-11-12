from Model.model import CalculatorModel
from View.view import CalculatorView

class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView()
        self.view.bind_add(lambda: self._on_op("add"))
        self.view.bind_sub(lambda: self._on_op("sub"))
        self.view.bind_mult(lambda: self._on_op("mult"))
        self.view.bind_div(lambda: self._on_op("div"))

    def _parse_inputs(self):
        a_str, b_str = self.view.get_inputs()
        try:
            a = float(a_str.replace(",", "."))
            b = float(b_str.replace(",", "."))
        except ValueError:
            raise ValueError("Please, enter valid numbers.")
        return a, b

    def _on_op(self, op: str):
        try:
            a, b = self._parse_inputs()
            if op == "add":
                res = self.model.add(a, b)
            elif op == "sub":
                res = self.model.sub(a, b)
            elif op == "mult":
                res = self.model.mult(a, b)
            elif op == "div":
                res = self.model.div(a, b)
            else:
                raise ValueError("Unknown operation.")
            self.view.show_result(res)
        except Exception as e:
            self.view.show_error(str(e))
    def run(self):
        self.view.run()
