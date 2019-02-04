function Y = clr(X)
% X: observation matrix, with rows represent observations, and columns
% variables
if iscolumn(X)
    X = X';
end
d = size(X, 2);
I = eye(d);
J = ones(d);
F = I - J/d;% F is for centering variables

Y = log(X)*F';% clr transform