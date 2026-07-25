function validate_hypergeom_params(N, K, n)
%VALIDATE_HYPERGEOM_PARAMS 检查 N, K, n 参数合法性

    if ~isscalar(N) || N <= 0 || floor(N) ~= N
        error('N 必须为正整数');
    end
    if ~isscalar(K) || K < 0 || K > N || floor(K) ~= K
        error('K 必须满足 0 <= K <= N');
    end
    if ~isscalar(n) || n < 0 || n > N || floor(n) ~= n
        error('n 必须满足 0 <= n <= N');
    end
end
