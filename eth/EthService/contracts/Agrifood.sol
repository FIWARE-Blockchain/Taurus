// SPDX-License-Identifier: MIT
pragma solidity >=0.4.21 <0.7.0;

contract Agrifood {
    struct _asset {
        string _id;
        string _name;
        string _type;
        string _description;
        string _owner;
        string _hasParent;
    }

    _asset[] public _assets;
    uint256 public _totalAssets;

    constructor() public {
        _totalAssets = 0;
    }

    event AssetEvent(
        string _id,
        string _name,
        string _type,
        string _desc,
        string _owner
    );

    function addAsset(
        string memory asset_id,
        string memory asset_name,
        string memory asset_type,
        string memory asset_desc,
        string memory asset_owner,
        string memory asset_parent
    ) public returns (uint256 _count) {
        _asset memory _newAsset = _asset(
            asset_id,
            asset_name,
            asset_type,
            asset_desc,
            asset_owner,
            asset_parent
        );
        _assets.push(_newAsset);
        _totalAssets++;
        emit AssetEvent(
            asset_id,
            asset_name,
            asset_type,
            asset_desc,
            asset_owner
        );
        return _totalAssets;
    }
}
