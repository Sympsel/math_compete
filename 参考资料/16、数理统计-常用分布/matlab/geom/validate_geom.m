function validate_geom(prob)
%VALIDATE_GEOM_PARAM 检查几何分布参数是否合法

    if ~isscalar(prob) || prob <= 0 || prob > 1
        error('成功概率 p 必须在 (0, 1] 区间内。');
    end
end
