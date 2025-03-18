#!/usr/bin/env python

# Capstone Python bindings, by Nguyen Anh Quynnh <aquynh@gmail.com>

from __future__ import print_function
from capstone import *
from capstone.aarch64 import *
from xprint import to_hex, to_x, to_x_32


AArch64_CODE = b"\x09\x00\x38\xd5\xbf\x40\x00\xd5\x0c\x05\x13\xd5\x20\x50\x02\x0e\x20\xe4\x3d\x0f\x00\x18\xa0\x5f\xa2\x00\xae\x9e\x9f\x37\x03\xd5\xbf\x33\x03\xd5\xdf\x3f\x03\xd5\x21\x7c\x02\x9b\x21\x7c\x00\x53\x00\x40\x21\x4b\xe1\x0b\x40\xb9\x20\x04\x81\xda\x20\x08\x02\x8b\x10\x5b\xe8\x3c\xfd\x7b\xba\xa9\xfd\xc7\x43\xf8"

all_tests = (
        (CS_ARCH_AARCH64, CS_MODE_ARM, AArch64_CODE, "AARCH64"),
        )


def print_insn_detail(insn):
    # print address, mnemonic and operands
    print("0x%x:\t%s\t%s" % (insn.address, insn.mnemonic, insn.op_str))

    # "data" instruction generated by SKIPDATA option has no detail
    if insn.id == 0:
        return

    if len(insn.operands) > 0:
        print("\top_count: %u" % len(insn.operands))
        c = -1
        for i in insn.operands:
            c += 1
            if i.type == AArch64_OP_REG:
                print("\t\toperands[%u].type: REG = %s" % (c, insn.reg_name(i.reg)))
            if i.type == AArch64_OP_IMM:
                print("\t\toperands[%u].type: IMM = 0x%s" % (c, to_x(i.imm)))
            if i.type == AArch64_OP_CIMM:
                print("\t\toperands[%u].type: C-IMM = %u" % (c, i.imm))
            if i.type == AArch64_OP_FP:
                print("\t\toperands[%u].type: FP = %f" % (c, i.fp))
            if i.type == AArch64_OP_MEM:
                print("\t\toperands[%u].type: MEM" % c)
                if i.mem.base != 0:
                    print("\t\t\toperands[%u].mem.base: REG = %s" \
                        % (c, insn.reg_name(i.mem.base)))
                if i.mem.index != 0:
                    print("\t\t\toperands[%u].mem.index: REG = %s" \
                        % (c, insn.reg_name(i.mem.index)))
                if i.mem.disp != 0:
                    print("\t\t\toperands[%u].mem.disp: 0x%s" \
                        % (c, to_x_32(i.mem.disp)))
                if insn.post_index:
                    print("\t\t\tpost-indexed: true");
            if i.type == AArch64_OP_SME_MATRIX:
                print("\t\toperands[%u].type: SME_MATRIX" % (c))
                print("\t\toperands[%u].sme.type: %d" % (c, i.sme.type))

                if i.sme.tile != AArch64_REG_INVALID:
                    print("\t\toperands[%u].sme.tile: %s" % (c, insn.reg_name(i.sme.tile)))
                if i.sme.slice_reg != AArch64_REG_INVALID:
                    print("\t\toperands[%u].sme.slice_reg: %s" % (c, insn.reg_name(i.sme.slice_reg)))
                if i.sme.slice_offset.imm != -1 or i.sme.slice_offset.imm_range.first != -1:
                    print("\t\toperands[%u].sme.slice_offset: " % (c))
                    if i.sme.has_range_offset:
                        print("%hhd:%hhd" % (i.sme.slice_offset.imm_range.first, i.sme.slice_offset.imm_range.offset))
                    else:
                        print("%d" % (i.sme.slice_offset.imm))
                if i.sme.slice_reg != AArch64_REG_INVALID or i.sme.slice_offset.imm != -1:
                    print("\t\toperands[%u].sme.is_vertical: %s" % (c, ("true" if i.sme.is_vertical else "false")))
            if i.type == AArch64_OP_SYSREG:
                print("\t\toperands[%u].type: SYS REG:" % (c))
                if i.sysop.sub_type == AArch64_OP_REG_MRS:
                    print("\t\toperands[%u].subtype: REG_MRS = 0x%x" % (c, i.sysop.reg.sysreg))
                if i.sysop.sub_type == AArch64_OP_REG_MSR:
                    print("\t\toperands[%u].subtype: REG_MSR = 0x%x" % (c, i.sysop.reg.sysreg))
                if i.sysop.sub_type == AArch64_OP_TLBI:
                    print("\t\toperands[%u].subtype TLBI = 0x%x" % (c, i.sysop.reg.tlbi))
                if i.sysop.sub_type == AArch64_OP_IC:
                    print("\t\toperands[%u].subtype IC = 0x%x" % (c, i.sysop.reg.ic))
            if i.type == AArch64_OP_SYSALIAS:
                print("\t\toperands[%u].type: SYS ALIAS:" % (c))
                if i.sysop.sub_type == AArch64_OP_SVCR:
                    if i.sysop.alias.svcr == AArch64_SVCR_SVCRSM:
                        print("\t\t\toperands[%u].svcr: BIT = SM" % (c))
                    elif i.sysop.alias.svcr == AArch64_SVCR_SVCRZA:
                        print("\t\t\toperands[%u].svcr: BIT = ZA" % (c))
                    elif i.sysop.alias.svcr == AArch64_SVCR_SVCRSMZA:
                        print("\t\t\toperands[%u].svcr: BIT = SM & ZA" % (c))
                if i.sysop.sub_type == AArch64_OP_AT:
                    print("\t\toperands[%u].subtype AT = 0x%x" % (c, i.sysop.alias.at))
                if i.sysop.sub_type == AArch64_OP_DB:
                    print("\t\toperands[%u].subtype DB = 0x%x" % (c, i.sysop.alias.db))
                if i.sysop.sub_type == AArch64_OP_DC:
                    print("\t\toperands[%u].subtype DC = 0x%x" % (c, i.sysop.alias.dc))
                if i.sysop.sub_type == AArch64_OP_ISB:
                    print("\t\toperands[%u].subtype ISB = 0x%x" % (c, i.sysop.alias.isb))
                if i.sysop.sub_type == AArch64_OP_TSB:
                    print("\t\toperands[%u].subtype TSB = 0x%x" % (c, i.sysop.alias.tsb))
                if i.sysop.sub_type == AArch64_OP_PRFM:
                    print("\t\toperands[%u].subtype PRFM = 0x%x" % (c, i.sysop.alias.prfm))
                if i.sysop.sub_type == AArch64_OP_SVEPRFM:
                    print("\t\toperands[%u].subtype SVEPRFM = 0x%x" % (c, i.sysop.alias.sveprfm))
                if i.sysop.sub_type == AArch64_OP_RPRFM:
                    print("\t\toperands[%u].subtype RPRFM = 0x%x" % (c, i.sysop.alias.rprfm))
                if i.sysop.sub_type == AArch64_OP_PSTATEIMM0_15:
                    print("\t\toperands[%u].subtype PSTATEIMM0_15 = 0x%x" % (c, i.sysop.alias.pstateimm0_15))
                if i.sysop.sub_type == AArch64_OP_PSTATEIMM0_1:
                    print("\t\toperands[%u].subtype PSTATEIMM0_1 = 0x%x" % (c, i.sysop.alias.pstateimm0_1))
                if i.sysop.sub_type == AArch64_OP_PSB:
                    print("\t\toperands[%u].subtype PSB = 0x%x" % (c, i.sysop.alias.psb))
                if i.sysop.sub_type == AArch64_OP_BTI:
                    print("\t\toperands[%u].subtype BTI = 0x%x" % (c, i.sysop.alias.bti))
                if i.sysop.sub_type == AArch64_OP_SVEPREDPAT:
                    print("\t\toperands[%u].subtype SVEPREDPAT = 0x%x" % (c, i.sysop.alias.svepredpat))
                if i.sysop.sub_type == AArch64_OP_SVEVECLENSPECIFIER:
                    print("\t\toperands[%u].subtype SVEVECLENSPECIFIER = 0x%x" % (c, i.sysop.alias.sveveclenspecifier))
            if i.type == AArch64_OP_SYSIMM:
                print("\t\toperands[%u].type: SYS IMM:" % (c))
                if i.sysop.sub_type == AArch64_OP_EXACTFPIMM:
                    print("\t\toperands[%u].subtype EXACTFPIMM = %d" % (c, i.sysop.imm.exactfpimm))
                if i.sysop.sub_type == AArch64_OP_DBNXS:
                    print("\t\toperands[%u].subtype DBNXS = %d" % (c, i.sysop.imm.dbnxs))

            if i.access == CS_AC_READ:
                print("\t\toperands[%u].access: READ" % (c))
            elif i.access == CS_AC_WRITE:
                print("\t\toperands[%u].access: WRITE" % (c))
            elif i.access == CS_AC_READ | CS_AC_WRITE:
                print("\t\toperands[%u].access: READ | WRITE" % (c))

            if i.shift.type != AArch64_SFT_INVALID and i.shift.value:
                print("\t\t\tShift: type = %u, value = %u" % (i.shift.type, i.shift.value))

            if i.ext != AArch64_EXT_INVALID:
                print("\t\t\tExt: %u" % i.ext)

            if i.vas != AArch64Layout_Invalid:
                print("\t\t\tVector Arrangement Specifier: 0x%x" % i.vas)

            if i.vector_index != -1:
                print("\t\t\tVector Index: %u" % i.vector_index)

    if insn.writeback:
        print("\tWrite-back: True")
            
    if not insn.cc in [AArch64CC_AL, AArch64CC_Invalid]:
        print("\tCode-condition: %u" % insn.cc)
    if insn.update_flags:
        print("\tUpdate-flags: True")

    (regs_read, regs_write) = insn.regs_access()

    if len(regs_read) > 0:
        print("\tRegisters read:", end="")
        for r in regs_read:
            print(" %s" %(insn.reg_name(r)), end="")
        print("")

    if len(regs_write) > 0:
        print("\tRegisters modified:", end="")
        for r in regs_write:
            print(" %s" %(insn.reg_name(r)), end="")
        print("")


# ## Test class Cs
def test_class():

    for (arch, mode, code, comment) in all_tests:
        print("*" * 16)
        print("Platform: %s" % comment)
        print("Code: %s" % to_hex(code))
        print("Disasm:")

        try:
            md = Cs(arch, mode)
            md.detail = True
            for insn in md.disasm(code, 0x2c):
                print_insn_detail(insn)
                print ()
            print("0x%x:\n" % (insn.address + insn.size))
        except CsError as e:
            print("ERROR: %s" % e)


if __name__ == '__main__':
    test_class()
