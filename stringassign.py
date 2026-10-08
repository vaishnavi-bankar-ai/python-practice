text = "X-DSPAM-Confidence:    0.8475"
task = text.find("0")
value= text[task : task+6]
print(float(value))