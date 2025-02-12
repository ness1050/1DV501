import MultiDisplay as multi

M = multi.MultiDisplay()
M.set_message("hello world!")
M.set_count(3)
print(M.to_string())                  # print-out
M.display()                           # print-out

M.set_display("Goodbye cruel world!", 2)    # print-out
print(M.to_string())                        # print-out
print("Current message:", M.get_message())