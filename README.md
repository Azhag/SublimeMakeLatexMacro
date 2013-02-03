Sublime Make Latex Macro
==============================


Small plugin to create Latex macro automatically in Sublime Text. 

Takes the current selection and creates a new command with a name provided by the user. Insert the command below a specific Latex comment anchor.

Example:
```
%New latex commands (auto)

[...]

x_i^t
```

```
(Make Latex Command) (Command name: xit)

%New latex commands (auto)
\newcommand{\xit}{x_i^t}

[...]

\xit
```

Not very tested and just because I'm lazy when creating Math macros and have a paper to write.