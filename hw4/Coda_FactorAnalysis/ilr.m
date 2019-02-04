function Z=ilr(X)
% X: observation matrix, with rows represent observations, and columns
% variables
[N, d] = size(X);
Z = zeros(N,d-1);
for i = 1:d-1
    fenzi = (prod(X(:, 1:i), 2)).^(1/i);
    Z(:, i) = sqrt(i/(i + 1))*log(fenzi./X(:, i + 1));
end