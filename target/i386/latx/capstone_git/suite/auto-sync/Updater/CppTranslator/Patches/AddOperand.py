from tree_sitter import Node

from CppTranslator.Patches.HelperMethods import get_text
from CppTranslator.Patches.Patch import Patch


class AddOperand(Patch):
    """
    Patch   MI.addOperand(...)
    to      MCInst_addOperand(MI, ...)
    """

    def __init__(self, priority: int):
        super().__init__(priority)

    def get_search_pattern(self) -> str:
        q = (
            "(call_expression "
            "   (field_expression"
            "       ((identifier) @inst_var)"
            '       ((field_identifier) @field_id_op (#eq? @field_id_op "addOperand"))'
            "   )"
            "   ((argument_list) @arg_list)"
            ") @add_operand"
        )
        return q

    def get_main_capture_name(self) -> str:
        return "add_operand"

    def get_patch(self, captures: [(Node, str)], src: bytes, **kwargs) -> bytes:
        # Get instruction variable name (MI, Inst)
        inst_var: Node = captures[1][0]
        # Arguments of getOperand(...)
        get_op_args = captures[3][0]
        inst = get_text(src, inst_var.start_byte, inst_var.end_byte)
        args = get_text(src, get_op_args.start_byte, get_op_args.end_byte)
        return b"MCInst_addOperand2(" + inst + b", " + args + b")"
