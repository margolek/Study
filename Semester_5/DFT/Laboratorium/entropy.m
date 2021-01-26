function e = entropy(x)
    p = x/sum(x);
    e = -sum( p .* log2(p) );
return 
