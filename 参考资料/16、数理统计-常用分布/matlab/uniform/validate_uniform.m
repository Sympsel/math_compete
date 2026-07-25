function validate_uniform(a, b)
%VALIDATE_UNIFORM_PARAM 检查 a 和 b 是否合法

    if ~isscalar(a) || ~isscalar(b) || b <= a
        error('参数必须满足 b > a');
    end
end
