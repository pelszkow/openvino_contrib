"""
 Copyright (C) 2018-2021 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from mo.front.common.partial_infer.utils import int64_array
from mo.front.extractor import FrontExtractorOp
from mo.ops.softmax import Softmax
from mo.utils.error import Error


class SoftmaxFrontExtractor(FrontExtractorOp):
    op = 'Softmax'
    enabled = True

    @classmethod
    def extract(cls, node):
        attrs = {
            'op': __class__.op,
            'axis': node.module.dim,
        }
        Softmax.update_node_stat(node, attrs)
        return cls.enabled
