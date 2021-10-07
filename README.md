# What is the higher value?

This is a exercise in Python really simple and interesting. You must only edit the list **S** to be the way you want it - understanding it as a table, with every _"\n"_ representing a linebreak. So every sequence of string before and after each
_"\n"_ is a differente line of this table, being the first one the titles line.

```Python
S = "id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7" # Edit this table
```

Or you can only create another list with your own table following the model and use it in the program.

<br>

### How does it work?

You must call the function **solution** and pass the parameters S and C as seen below:

```Python
solution(S, C)
```

- **S** - The table in string format, as in the model.
- **C** - The parameter you want to filter in the table to find the higher value.

<br>

#### Example: 

<br>

```Python
table = "id,name,age\n1,Gabriel,23\n2,Beatriz,22"
```

<br>

| id | name    | age |
|----|---------|-----|
| 1  | Gabriel | 23  |
| 2  | Beatriz | 22  |

<br>

So you must do like:

```Python
print(solution(table, "age"))
```

And the return will be 23 because in the field "age" of the table, 23 is the higher.

<br>
<br>

# OBS

This project is recommended to be used only for those who at least know how to run a Python project and basic coding.

<br>

> Follow me: [Instagram](https://instagram.com/eugaoliver), [LinkedIn](https://linkedin.com/in/gabrielocramos), [Twitter](https://twitter.com/eugaoliver)
